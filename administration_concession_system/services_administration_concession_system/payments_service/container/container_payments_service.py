from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Payments Service - Container Diagram", direction="TB"):
    with SystemBoundary("Administration Concession System"):
        
        # Payments Service
        payments_service = Container(
            "Payments Service",
            ".NET",
            "Manages and processes payments within the concession system"
        )
        
        # Command Side (CQRS)
        with SystemBoundary("Command Side"):
            process_payment_command = Container(
                "ProcessPaymentCommand",
                "Command",
                "Handles requests to process payments"
            )

            refund_payment_command = Container(
                "RefundPaymentCommand",
                "Command",
                "Handles requests to refund payments"
            )
        
        # Query Side (CQRS)
        with SystemBoundary("Query Side"):
            get_payment_summary_query = Container(
                "GetPaymentSummaryQuery",
                "Query",
                "Fetches a summary of payments"
            )

            get_payment_details_query = Container(
                "GetPaymentDetailsQuery",
                "Query",
                "Fetches detailed payment information"
            )

        # Domain Events
        with SystemBoundary("Events"):
            payment_processed_event = Container(
                "PaymentProcessedEvent",
                "Event",
                "Published when a payment is successfully processed"
            )

            payment_refunded_event = Container(
                "PaymentRefundedEvent",
                "Event",
                "Published when a payment is refunded"
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
        payments_db = Database(
            "Payments Database",
            "MongoDB",
            "Stores payment-related data"
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
        payments_service >> Relationship("Handles") >> process_payment_command
        payments_service >> Relationship("Handles") >> refund_payment_command
        
        process_payment_command >> Relationship("Executes business logic via") >> payments_service
        refund_payment_command >> Relationship("Executes business logic via") >> payments_service

        # Relationships - Query Side
        payments_service >> Relationship("Handles") >> get_payment_summary_query
        payments_service >> Relationship("Handles") >> get_payment_details_query
        
        get_payment_summary_query >> Relationship("Executes business logic via") >> payments_service
        get_payment_details_query >> Relationship("Executes business logic via") >> payments_service

        # Supporting Services and Event Publishing
        payments_service >> Relationship("Validates permissions with") >> auth_service
        payments_service >> Relationship("Reads from/Writes to") >> payments_db
        payments_service >> Relationship("Publishes events via") >> event_publisher
        
        event_publisher >> Relationship("Publishes") >> [
            payment_processed_event, 
            payment_refunded_event
        ]
        
        # Event flow within the system
        payment_processed_event >> Relationship("Sent via") >> internal_event_bus
        payment_refunded_event >> Relationship("Sent via") >> internal_event_bus
        
        internal_event_bus >> Relationship("Forwards events to") >> external_event_bus

        # CRM System
        with SystemBoundary("CRM System"):
            leads_service_crm = Container(
                "Leads Summary Service",
                ".NET",
                "Handles and stores payment-related data from the Administration Concession System"
            )

            facturation_service_crm = Container(
                "Facturation Service",
                ".NET",
                "Handles invoicing and billing for payments from the Administration Concession System"
            )

            orders_service_crm = Container(
                "Orders Summary Service",
                ".NET",
                "Handles and stores order-related payment data from the Administration Concession System"
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

            crm_db_facturation = Database(
                "Facturation Database",
                "MongoDB",
                "Stores invoicing and billing data"
            )

            crm_db_orders = Database(
                "Orders Database",
                "MongoDB",
                "Stores order-related payment data"
            )
            
            external_event_bus >> Relationship("Forwards payment data to") >> [leads_service_crm, facturation_service_crm, orders_service_crm]
            leads_service_crm >> Relationship("Stores data in") >> crm_db_leads
            facturation_service_crm >> Relationship("Stores data in") >> crm_db_facturation
            orders_service_crm >> Relationship("Stores data in") >> crm_db_orders
            leads_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
            facturation_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
            orders_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
