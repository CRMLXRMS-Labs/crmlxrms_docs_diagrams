from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Authorization Microservice - Detailed Container Diagram with RegisterConcessionCommand", direction="TB"):
    with SystemBoundary("Administration Concession System"):
        # Authorization Microservice
        auth_service = Container(
            "Authorization Microservice",
            "ASP.NET Core",
            "Handles authentication, authorization, and registration of concessions"
        )

        admin_internal_operations_service = Container(
            "Administration Concession Internal Opertaions Microservice",
            "ASP.NET Core",
            "Translates all operations performed in administration concession system"
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
            
            refresh_access_token_command = Container(
                "RefreshAccessTokenCommand",
                "Command",
                "Revokes deactivated user's access token"
            )
            
            reset_password_command = Container(
                "ResetPasswordCommand",
                "Command",
                "Resets the user's password"
            )
            
            enable_2fa_command = Container(
                "Enable2FACommand",
                "Command",
                "Enables Two-Factor Authentication for the user"
            )
            
            disable_2fa_command = Container(
                "Disable2FACommand",
                "Command",
                "Disables Two-Factor Authentication for the user"
            )

            verify_email_command = Container(
                "VerifyEmailCommand",
                "Command",
                "Initiates email verification process"
            )

            register_concession_command = Container(
                "RegisterConcessionCommand",
                "Command",
                "Registers a new concession in the system"
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
            
            get_2fa_status_query = Container(
                "Get2FAStatusQuery",
                "Query",
                "Fetches the 2FA status of a user"
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
            
            two_factor_enabled_event = Container(
                "TwoFactorEnabledEvent",
                "Event",
                "Published when a user enables 2FA"
            )
            
            two_factor_disabled_event = Container(
                "TwoFactorDisabledEvent",
                "Event",
                "Published when a user disables 2FA"
            )
            
            email_verified_event = Container(
                "EmailVerifiedEvent",
                "Event",
                "Published when a user's email is successfully verified"
            )
            
            email_verification_failed_event = Container(
                "EmailVerificationFailedEvent",
                "Event",
                "Published when a user's email verification fails"
            )

            concession_registered_event = Container(
                "ConcessionRegisteredEvent",
                "Event",
                "Published when a new concession is registered"
            )

        # Supporting Components
        auth_service_logic = Container(
            "AuthService",
            "ASP.NET Core",
            "Business logic for authentication, authorization, and concession registration"
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
        internal_event_bus = Container("Internal Event Bus", "RabbitMQ", "Internal communication within Administration Concession System")
        external_event_bus = Container(" CRM External Event Bus", "RabbitMQ", "Communication with CRM")

        # Relationships - Command Side
        auth_service >> Relationship("Handles") >> user_login_command
        auth_service >> Relationship("Handles") >> user_logout_command
        auth_service >> Relationship("Handles") >> revoke_access_token_command
        auth_service >> Relationship("Handles") >> refresh_access_token_command
        auth_service >> Relationship("Handles") >> reset_password_command
        auth_service >> Relationship("Handles") >> enable_2fa_command
        auth_service >> Relationship("Handles") >> disable_2fa_command
        auth_service >> Relationship("Handles") >> verify_email_command
        auth_service >> Relationship("Handles") >> register_concession_command
        
        user_login_command >> Relationship("Executes business logic via") >> auth_service_logic
        user_logout_command >> Relationship("Executes business logic via") >> auth_service_logic
        revoke_access_token_command >> Relationship("Executes business logic via") >> auth_service_logic
        refresh_access_token_command >> Relationship("Destroy access revoce destroy access token for user") >> auth_service_logic
        reset_password_command >> Relationship("Executes business logic via") >> auth_service_logic
        enable_2fa_command >> Relationship("Executes business logic via") >> auth_service_logic
        disable_2fa_command >> Relationship("Executes business logic via") >> auth_service_logic
        verify_email_command >> Relationship("Executes business logic via") >> auth_service_logic
        register_concession_command >> Relationship("Executes business logic via") >> auth_service_logic

        # Relationships - Query Side
        auth_service >> Relationship("Handles") >> get_user_permissions_query
        auth_service >> Relationship("Handles") >> get_user_details_query
        auth_service >> Relationship("Handles") >> get_2fa_status_query
        
        get_user_permissions_query >> Relationship("Executes business logic via") >> auth_service_logic
        get_user_details_query >> Relationship("Executes business logic via") >> auth_service_logic
        get_2fa_status_query >> Relationship("Executes business logic via") >> auth_service_logic

        # Supporting Services and Event Publishing
        auth_service_logic >> Relationship("Interacts with JWT via") >> jwt_service
        auth_service_logic >> Relationship("Reads from/Writes to") >> auth_db
        auth_service_logic >> Relationship("Publishes events via") >> event_publisher
        
        event_publisher >> Relationship("Publishes") >> [
            user_logged_in_event, 
            user_logged_out_event, 
            password_reset_event, 
            two_factor_enabled_event, 
            two_factor_disabled_event, 
            email_verified_event, 
            email_verification_failed_event,
            concession_registered_event
        ]
        
        user_logged_in_event >> Relationship("Sent via") >> internal_event_bus
        user_logged_out_event >> Relationship("Sent via") >> internal_event_bus
        password_reset_event >> Relationship("Sent via") >> internal_event_bus
        two_factor_enabled_event >> Relationship("Sent via") >> internal_event_bus
        two_factor_disabled_event >> Relationship("Sent via") >> internal_event_bus
        email_verified_event >> Relationship("Sent via") >> internal_event_bus
        email_verification_failed_event >> Relationship("Sent via") >> internal_event_bus
        concession_registered_event >> Relationship("Sent via") >> internal_event_bus
        
        internal_event_bus >> Relationship("Forwards events to") >> external_event_bus
        
        # Leads Summary Service in CRM
        leads_service_crm = Container(
            "CRM Leads Summary Service",
            ".NET",
            "Stores data of users from the Administration Concession System"
        )
        operations_internal_service_crm = Container(
            "CRM Internal Operations Service",
            ".NET",
            "Works out the data of each opearation in Administration Concession System to CRM System"
        )
        auth_service >> Relationship("Forwards data to") >> admin_internal_operations_service
        admin_internal_operations_service >> Relationship("Forwards data to") >> operations_internal_service_crm

        operations_internal_service_crm >> Relationship("Stores data in") >> Database(
            "CRM Internal Operations Database",
            "MongoDB",
            "Stores operations data, from Administration Concession System"
        )
        
        external_event_bus >> Relationship("Forwards user data to") >> leads_service_crm
        leads_service_crm >> Relationship("Stores data in") >> Database(
            "CRM Leads Database",
            "MongoDB",
            "Stores lead-related data, including users from Administration Concession System"
        )
        
        # SignalR Hub for Real-Time Updates
        signalr_hub = Container(
            "CRM  leads SignalR Hub",
            "ASP.NET Core",
            "Real-time communication hub for notifying CRM users of online leads"
        )

        user_crm = Container(
            "CRM User",
            "User",
            "User in CRM system receiving updates"
        )
        
        leads_service_crm >> Relationship("Notifies via") >> signalr_hub
        signalr_hub >> Relationship("Updates CRM users in real-time") >> user_crm
        operations_internal_service_crm >>  Relationship("Translates users' operaions data in real-time") >> user_crm

        
