from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Internal Statistics Service - Container Diagram", direction="TB"):
    with SystemBoundary("Administration Concession System"):
        
        # Internal Statistics Service
        internal_statistics_service = Container(
            "Internal Statistics Service",
            ".NET",
            "Processes and provides internal statistics like user activity and system health"
        )
        
        # Command Side (CQRS)
        with SystemBoundary("Command Side"):
            generate_statistics_command = Container(
                "GenerateStatisticsCommand",
                "Command",
                "Handles requests to generate new internal statistics"
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
                "Fetches summaries of generated internal statistics"
            )

            get_statistics_details_query = Container(
                "GetStatisticsDetailsQuery",
                "Query",
                "Fetches detailed information on specific internal statistics"
            )

        # Supporting Components
        auth_service = Container(
            "Authorization Microservice",
            "ASP.NET Core",
            "Handles user authentication and authorization"
        )

        # Databases and Event Buses
        internal_statistics_db = Database(
            "Internal Statistics Database",
            "MongoDB",
            "Stores data related to generated internal statistics"
        )

        # Relationships - Command Side
        internal_statistics_service >> Relationship("Handles") >> generate_statistics_command
        internal_statistics_service >> Relationship("Handles") >> update_statistics_command
        internal_statistics_service >> Relationship("Handles") >> delete_statistics_command
        
        generate_statistics_command >> Relationship("Executes business logic via") >> internal_statistics_service
        update_statistics_command >> Relationship("Executes business logic via") >> internal_statistics_service
        delete_statistics_command >> Relationship("Executes business logic via") >> internal_statistics_service

        # Relationships - Query Side
        internal_statistics_service >> Relationship("Handles") >> get_statistics_summary_query
        internal_statistics_service >> Relationship("Handles") >> get_statistics_details_query
        
        get_statistics_summary_query >> Relationship("Executes business logic via") >> internal_statistics_service
        get_statistics_details_query >> Relationship("Executes business logic via") >> internal_statistics_service

        # Supporting Services and Data Handling
        internal_statistics_service >> Relationship("Validates permissions with") >> auth_service
        internal_statistics_service >> Relationship("Reads from/Writes to") >> internal_statistics_db

        # CRM System
        with SystemBoundary("CRM System"):
            crm_internal_statistics_service = Container(
                "CRM Internal Statistics Service",
                ".NET",
                "Generates and provides internal statistics related to customer interactions"
            )

            ml_service = Container(
                "ML Service",
                "ML.NET",
                "Performs machine learning-based analytics and predictions"
            )

            leads_service = Container(
                "Leads Service",
                ".NET",
                "Manages and tracks lead information within the CRM"
            )
            
            crm_db = Database(
                "CRM Database",
                "MongoDB",
                "Stores lead and statistics-related data"
            )
            
            crm_internal_statistics_service >> Relationship("Provides internal statistics data to") >> internal_statistics_service
            ml_service >> Relationship("Provides analytics insights to") >> internal_statistics_service
            leads_service >> Relationship("Supplies lead data for analysis to") >> internal_statistics_service
            
            internal_statistics_service >> Relationship("Aggregates data from") >> crm_db
