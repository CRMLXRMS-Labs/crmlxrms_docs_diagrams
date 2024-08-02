from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Operation gRPC Service - Container Diagram", direction="TB"):
    with SystemBoundary("Administration Concession System"):
        
        # Operation gRPC Service
        operation_grpc_service = Container(
            "Operation gRPC Service",
            "gRPC",
            "Handles user operations and communicates with the CRM system"
        )
        
        # User Operations
        with SystemBoundary("User Operations"):
            user_login_operation = Container(
                "UserLoginOperation",
                "gRPC",
                "Handles user login operations"
            )

            view_statistics_operation = Container(
                "ViewStatisticsOperation",
                "gRPC",
                "Handles viewing of statistics and data"
            )

            perform_action_operation = Container(
                "PerformActionOperation",
                "gRPC",
                "Handles other user actions within the Admin Concession System"
            )
        
        # Supporting Components
        auth_service = Container(
            "Authorization Microservice",
            "ASP.NET Core",
            "Handles user authentication and authorization"
        )

        # Databases
        operation_db = Database(
            "Operation Database",
            "MongoDB",
            "Stores data related to all operations"
        )

        # Relationships - User Operations
        operation_grpc_service >> Relationship("Handles") >> user_login_operation
        operation_grpc_service >> Relationship("Handles") >> view_statistics_operation
        operation_grpc_service >> Relationship("Handles") >> perform_action_operation
        
        user_login_operation >> Relationship("Executes") >> operation_grpc_service
        view_statistics_operation >> Relationship("Executes") >> operation_grpc_service
        perform_action_operation >> Relationship("Executes") >> operation_grpc_service

        # Supporting Services and Data Handling
        operation_grpc_service >> Relationship("Validates permissions with") >> auth_service
        operation_grpc_service >> Relationship("Reads from/Writes to") >> operation_db

        # CRM System
        with SystemBoundary("CRM System"):
            external_operations_service = Container(
                "External Operations Service",
                ".NET",
                "Handles external operations and integrates data from Operation gRPC Service"
            )
            
            crm_db = Database(
                "CRM Database",
                "MongoDB",
                "Stores customer and operational data"
            )
            
            operation_grpc_service >> Relationship("Sends operational data to") >> external_operations_service
            external_operations_service >> Relationship("Stores data in") >> crm_db
            external_operations_service >> Relationship("Processes and provides data to") >> view_statistics_operation
