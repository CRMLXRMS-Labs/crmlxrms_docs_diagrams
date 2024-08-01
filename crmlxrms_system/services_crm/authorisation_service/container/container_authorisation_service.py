from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Authorization Microservice - Detailed Container Diagram", direction="TB"):
    with SystemBoundary("CRM System"):
        # Authorization Microservice
        auth_service = Container(
            "Authorization Microservice",
            "ASP.NET Core",
            "Handles authentication and authorization"
        )

        # Command Side (CQRS)
        with SystemBoundary("Command Side"):
            user_login_command = Container(
                "UserLoginCommand",
                "Command",
                "Initiates user login process"
            )

            user_logout_command = Container(
                "UserLogoutCommand",
                "Command",
                "Initiates user logout process"
            )
            
            revoke_access_token_command = Container(
                "RevokeAccessTokenCommand",
                "Command",
                "Revokes a user's access token"
            )
            
            reset_password_command = Container(
                "ResetPasswordCommand",
                "Command",
                "Resets the user's password"
            )

        # Query Side (CQRS)
        with SystemBoundary("Query Side"):
            get_user_permissions_query = Container(
                "GetUserPermissionsQuery",
                "Query",
                "Fetches the permissions associated with a user"
            )

            get_user_details_query = Container(
                "GetUserDetailsQuery",
                "Query",
                "Fetches the details of a user"
            )

        # Domain Events
        with SystemBoundary("Events"):
            user_logged_in_event = Container(
                "UserLoggedInEvent",
                "Event",
                "Published when a user successfully logs in"
            )

            user_logged_out_event = Container(
                "UserLoggedOutEvent",
                "Event",
                "Published when a user logs out"
            )
            
            password_reset_event = Container(
                "PasswordResetEvent",
                "Event",
                "Published when a user's password is reset"
            )

        # Supporting Components
        auth_service_logic = Container(
            "AuthService",
            "ASP.NET Core",
            "Business logic for authentication and authorization"
        )

        jwt_service = Container(
            "JWT Service",
            "ASP.NET Core",
            "Generates and validates JWT tokens"
        )

        event_publisher = Container(
            "Event Publisher",
            "ASP.NET Core with RabbitMQ",
            "Publishes domain events to the event bus"
        )
        
        # Databases and Event Buses
        auth_db = Database("Auth Database", "MongoDB", "Stores user credentials and authorization data")
        internal_event_bus = Container("Internal Event Bus", "RabbitMQ", "Internal communication within CRM")
        external_event_bus = Container("External Event Bus", "RabbitMQ", "Communication with other systems")

        # Relationships - Command Side
        auth_service >> Relationship("Handles") >> user_login_command
        auth_service >> Relationship("Handles") >> user_logout_command
        auth_service >> Relationship("Handles") >> revoke_access_token_command
        auth_service >> Relationship("Handles") >> reset_password_command
        
        user_login_command >> Relationship("Executes business logic via") >> auth_service_logic
        user_logout_command >> Relationship("Executes business logic via") >> auth_service_logic
        revoke_access_token_command >> Relationship("Executes business logic via") >> auth_service_logic
        reset_password_command >> Relationship("Executes business logic via") >> auth_service_logic

        # Relationships - Query Side
        auth_service >> Relationship("Handles") >> get_user_permissions_query
        auth_service >> Relationship("Handles") >> get_user_details_query
        
        get_user_permissions_query >> Relationship("Executes business logic via") >> auth_service_logic
        get_user_details_query >> Relationship("Executes business logic via") >> auth_service_logic

        # Supporting Services and Event Publishing
        auth_service_logic >> Relationship("Interacts with JWT via") >> jwt_service
        auth_service_logic >> Relationship("Reads from/Writes to") >> auth_db
        auth_service_logic >> Relationship("Publishes events via") >> event_publisher
        
        event_publisher >> Relationship("Publishes") >> [user_logged_in_event, user_logged_out_event, password_reset_event]
        user_logged_in_event >> Relationship("Sent via") >> internal_event_bus
        user_logged_out_event >> Relationship("Sent via") >> internal_event_bus
        password_reset_event >> Relationship("Sent via") >> internal_event_bus
        
        internal_event_bus >> Relationship("Forwards events to") >> external_event_bus
