from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("External Statistics Service - Container Diagram", direction="TB"):
    with SystemBoundary("Administration Concession System"):
        
        # External Statistics Service
        external_statistics_service = Container(
            "External Statistics Service",
            ".NET",
            "Generates statistics like behavior analysis, risk assessment, and trend analysis"
        )
        
        # Command Side (CQRS)
        with SystemBoundary("Command Side"):
            generate_statistics_command = Container(
                "GenerateStatisticsCommand",
                "Command",
                "Handles requests to generate new statistics based on client data"
            )

            update_statistics_command = Container(
                "UpdateStatisticsCommand",
                "Command",
                "Handles requests to update existing statistics"
            )

            delete_statistics_command = Container(
                "DeleteStatisticsCommand",
                "Command",
                "Handles requests to delete specific statistics"
            )
        
        # Query Side (CQRS)
        with SystemBoundary("Query Side"):
            get_statistics_summary_query = Container(
                "GetStatisticsSummaryQuery",
                "Query",
                "Fetches summaries of the generated statistics"
            )

            get_statistics_details_query = Container(
                "GetStatisticsDetailsQuery",
                "Query",
                "Fetches detailed information on specific statistics"
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
            "Stores data related to generated statistics"
        )
        
        internal_event_bus = Container(
            "Internal Event Bus",
            "RabbitMQ",
            "Facilitates internal communication within the concession system"
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
            crm_integration_service = Container(
                "CRM Integration Service",
                ".NET",
                "Integrates statistics data with CRM system"
            )

            ml_service = Container(
                "ML Service",
                "ML.NET",
                "Provides machine learning-based analytics and predictions"
            )

            facturation_service = Container(
                "Facturation Service",
                ".NET",
                "Manages invoicing and payment processing"
            )
            
            external_statistics_service_crm = Container(
                "External Statistics Service",
                ".NET",
                "Handles external statistics for CRM"
            )
            
            crm_db = Database(
                "CRM Database",
                "MongoDB",
                "Stores client and statistics-related data"
            )
            
            external_event_bus >> Relationship("Forwards statistics data to") >> [
                crm_integration_service, 
                ml_service, 
                facturation_service, 
                external_statistics_service_crm
            ]
            crm_integration_service >> Relationship("Stores data in") >> crm_db
            ml_service >> Relationship("Processes data and returns insights to") >> crm_integration_service
            facturation_service >> Relationship("Uses statistics for generating invoices") >> crm_integration_service
            external_statistics_service_crm >> Relationship("Uses statistics to generate reports") >> crm_integration_service
