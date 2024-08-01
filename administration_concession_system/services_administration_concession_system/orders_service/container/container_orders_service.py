from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Orders Service - Container Diagram", direction="TB"):
    with SystemBoundary("Administration Concession System"):
        
        # Orders Service
        orders_service = Container(
            "Orders Service",
            ".NET",
            "Manages and provides information related to orders"
        )
        
        # Command Side (CQRS)
        with SystemBoundary("Command Side"):
            create_order_command = Container(
                "CreateOrderCommand",
                "Command",
                "Handles requests to create a new order"
            )

            update_order_command = Container(
                "UpdateOrderCommand",
                "Command",
                "Handles requests to update order information"
            )

            cancel_order_command = Container(
                "CancelOrderCommand",
                "Command",
                "Handles requests to cancel an order"
            )
        
        # Query Side (CQRS)
        with SystemBoundary("Query Side"):
            get_order_summary_query = Container(
                "GetOrderSummaryQuery",
                "Query",
                "Fetches a summary of a user's orders"
            )

            get_order_details_query = Container(
                "GetOrderDetailsQuery",
                "Query",
                "Fetches detailed order information"
            )

        # Domain Events
        with SystemBoundary("Events"):
            order_created_event = Container(
                "OrderCreatedEvent",
                "Event",
                "Published when a new order is created"
            )

            order_updated_event = Container(
                "OrderUpdatedEvent",
                "Event",
                "Published when an order is updated"
            )
            
            order_cancelled_event = Container(
                "OrderCancelledEvent",
                "Event",
                "Published when an order is cancelled"
            )

        # Supporting Components
        auth_service = Container(
            "Authorization Microservice",
            "ASP.NET Core",
            "Handles user authentication and authorization"
        )

        event_publisher = Container(
            "Event Publisher",
            "ASP.NET Core with RabbitMQ",
            "Publishes domain events to the event bus"
        )

        # Databases and Event Buses
        orders_db = Database(
            "Orders Database",
            "MongoDB",
            "Stores order-related data"
        )
        
        internal_event_bus = Container(
            "Internal Event Bus",
            "RabbitMQ",
            "Handles internal communication within the Administration Concession System"
        )
        
        external_event_bus = Container(
            "External Event Bus",
            "RabbitMQ",
            "Handles communication with the CRM system"
        )

        # Relationships - Command Side
        orders_service >> Relationship("Handles") >> create_order_command
        orders_service >> Relationship("Handles") >> update_order_command
        orders_service >> Relationship("Handles") >> cancel_order_command
        
        create_order_command >> Relationship("Executes business logic via") >> orders_service
        update_order_command >> Relationship("Executes business logic via") >> orders_service
        cancel_order_command >> Relationship("Executes business logic via") >> orders_service

        # Relationships - Query Side
        orders_service >> Relationship("Handles") >> get_order_summary_query
        orders_service >> Relationship("Handles") >> get_order_details_query
        
        get_order_summary_query >> Relationship("Executes business logic via") >> orders_service
        get_order_details_query >> Relationship("Executes business logic via") >> orders_service

        # Supporting Services and Event Publishing
        orders_service >> Relationship("Validates permissions with") >> auth_service
        orders_service >> Relationship("Reads from/Writes to") >> orders_db
        orders_service >> Relationship("Publishes events via") >> event_publisher
        
        event_publisher >> Relationship("Publishes") >> [
            order_created_event, 
            order_updated_event, 
            order_cancelled_event
        ]
        
        # Event flow within the system
        order_created_event >> Relationship("Sent via") >> internal_event_bus
        order_updated_event >> Relationship("Sent via") >> internal_event_bus
        order_cancelled_event >> Relationship("Sent via") >> internal_event_bus
        
        internal_event_bus >> Relationship("Forwards events to") >> external_event_bus

        # CRM System
        with SystemBoundary("CRM System"):
            leads_service_crm = Container(
                "Leads Summary Service",
                ".NET",
                "Handles and stores lead-related data from the Administration Concession System"
            )

            orders_summary_service_crm = Container(
                "Orders Summary Service",
                ".NET",
                "Handles and stores order-related data from the Administration Concession System"
            )
            
            crm_event_publisher = Container(
                "CRM Event Publisher",
                "ASP.NET Core with RabbitMQ",
                "Publishes events to CRM event bus"
            )
            
            crm_db_leads = Database(
                "Leads Database",
                "MongoDB",
                "Stores lead-related data"
            )

            crm_db_orders = Database(
                "Orders Database",
                "MongoDB",
                "Stores order-related data"
            )
            
            external_event_bus >> Relationship("Forwards order data to") >> [leads_service_crm, orders_summary_service_crm]
            leads_service_crm >> Relationship("Stores data in") >> crm_db_leads
            orders_summary_service_crm >> Relationship("Stores data in") >> crm_db_orders
            leads_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
            orders_summary_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
