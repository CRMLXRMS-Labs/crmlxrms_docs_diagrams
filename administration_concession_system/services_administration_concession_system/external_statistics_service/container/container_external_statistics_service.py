from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("External Statistics Service - Container Diagram", direction="TB"):
    with SystemBoundary("Administration Concession System"):
        
        # External Statistics Service
        external_statistics_service = Container(
            "External Statistics Service",
            ".NET",
            "Provides external statistics and analytics"
        )
        
        # Command Side (CQRS)
        with SystemBoundary("Command Side"):
            generate_statistics_command = Container(
                "GenerateStatisticsCommand",
                "Command",
                "Handles requests to generate new statistics"
            )

            update_statistics_command = Container(
                "UpdateStatisticsCommand",
                "Command",
                "Handles requests to update statistics"
            )

            delete_statistics_command = Container(
                "DeleteStatisticsCommand",
                "Command",
                "Handles requests to delete statistics"
            )
        
        # Query Side (CQRS)
        with SystemBoundary("Query Side"):
            get_statistics_summary_query = Container(
                "GetStatisticsSummaryQuery",
                "Query",
                "Fetches a summary of the statistics"
            )

            get_statistics_details_query = Container(
                "GetStatisticsDetailsQuery",
                "Query",
                "Fetches detailed statistics information"
            )

        # Domain Events
        with SystemBoundary("Events"):
            statistics_generated_event = Container(
                "StatisticsGeneratedEvent",
                "Event",
                "Published when new statistics are generated"
            )

            statistics_updated_event = Container(
                "StatisticsUpdatedEvent",
                "Event",
                "Published when statistics are updated"
            )
            
            statistics_deleted_event = Container(
                "StatisticsDeletedEvent",
                "Event",
                "Published when statistics are deleted"
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
        statistics_db = Database(
            "Statistics Database",
            "MongoDB",
            "Stores statistics-related data"
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
        external_statistics_service >> Relationship("Handles") >> generate_statistics_command
        external_statistics_service >> Relationship("Handles") >> update_statistics_command
        external_statistics_service >> Relationship("Handles") >> delete_statistics_command
        
        generate_statistics_command >> Relationship("Executes business logic via") >> external_statistics_service
        update_statistics_command >> Relationship("Executes business logic via") >> external_statistics_service
        delete_statistics_command >> Relationship("Executes business logic via") >> external_statistics_service

        # Relationships - Query Side
        external_statistics_service >> Relationship("Handles") >> get_statistics_summary_query
        external_statistics_service >> Relationship("Handles") >> get_statistics_details_query
        
        get_statistics_summary_query >> Relationship("Executes business logic via") >> external_statistics_service
        get_statistics_details_query >> Relationship("Executes business logic via") >> external_statistics_service

        # Supporting Services and Event Publishing
        external_statistics_service >> Relationship("Validates permissions with") >> auth_service
        external_statistics_service >> Relationship("Reads from/Writes to") >> statistics_db
        external_statistics_service >> Relationship("Publishes events via") >> event_publisher
        
        event_publisher >> Relationship("Publishes") >> [
            statistics_generated_event, 
            statistics_updated_event, 
            statistics_deleted_event
        ]
        
        # Event flow within the system
        statistics_generated_event >> Relationship("Sent via") >> internal_event_bus
        statistics_updated_event >> Relationship("Sent via") >> internal_event_bus
        statistics_deleted_event >> Relationship("Sent via") >> internal_event_bus
        
        internal_event_bus >> Relationship("Forwards events to") >> external_event_bus

        # CRM System
        with SystemBoundary("CRM System"):
            leads_service_crm = Container(
                "Leads Summary Service",
                ".NET",
                "Handles and stores statistics-related data from the Administration Concession System"
            )

            orders_summary_service_crm = Container(
                "Orders Summary Service",
                ".NET",
                "Handles and stores order-related statistics data from the Administration Concession System"
            )

            facturation_service_crm = Container(
                "Facturation Service",
                ".NET",
                "Handles invoicing and billing data related to statistics from the Administration Concession System"
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

            crm_db_facturation = Database(
                "Facturation Database",
                "MongoDB",
                "Stores invoicing and billing data"
            )
            
            external_event_bus >> Relationship("Forwards statistics data to") >> [leads_service_crm, orders_summary_service_crm, facturation_service_crm]
            leads_service_crm >> Relationship("Stores data in") >> crm_db_leads
            orders_summary_service_crm >> Relationship("Stores data in") >> crm_db_orders
            facturation_service_crm >> Relationship("Stores data in") >> crm_db_facturation
            leads_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
            orders_summary_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
            facturation_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
