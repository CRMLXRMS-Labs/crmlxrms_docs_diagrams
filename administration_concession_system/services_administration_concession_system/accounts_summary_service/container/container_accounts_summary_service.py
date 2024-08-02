from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Accounts Summary Service - Complex Container Diagram", direction="TB"):
    with SystemBoundary("Administration Concession System"):
        
        # Accounts Summary Service
        accounts_service = Container(
            "Accounts Summary Service",
            ".NET",
            "Provides users with a summary of their accounts"
        )
        
        # Command Side (CQRS)
        with SystemBoundary("Command Side"):
            create_account_command = Container(
                "CreateAccountCommand",
                "Command",
                "Handles requests to create a new account"
            )

            update_account_command = Container(
                "UpdateAccountCommand",
                "Command",
                "Handles requests to update account information"
            )
            
            deactivate_account_command = Container(
                "DeactivateAccountCommand",
                "Command",
                "Handles requests to deactivate an account"
            )
            
            verify_account_command = Container(
                "VerifyAccountCommand",
                "Command",
                "Handles requests to verify an account"
            )
        
        # Query Side (CQRS)
        with SystemBoundary("Query Side"):
            get_account_summary_query = Container(
                "GetAccountSummaryQuery",
                "Query",
                "Fetches a summary of a user's account"
            )

            get_account_details_query = Container(
                "GetAccountDetailsQuery",
                "Query",
                "Fetches detailed account information"
            )

        # Domain Events
        with SystemBoundary("Events"):
            account_created_event = Container(
                "AccountCreatedEvent",
                "Event",
                "Published when a new account is created"
            )

            account_updated_event = Container(
                "AccountUpdatedEvent",
                "Event",
                "Published when an account is updated"
            )
            
            account_deactivated_event = Container(
                "AccountDeactivatedEvent",
                "Event",
                "Published when an account is deactivated"
            )
            
            account_verified_event = Container(
                "AccountVerifiedEvent",
                "Event",
                "Published when an account is verified"
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
        accounts_db = Database(
            "Accounts Database",
            "MongoDB",
            "Stores account-related data"
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
        accounts_service >> Relationship("Handles") >> create_account_command
        accounts_service >> Relationship("Handles") >> update_account_command
        accounts_service >> Relationship("Handles") >> deactivate_account_command
        accounts_service >> Relationship("Handles") >> verify_account_command
        
        create_account_command >> Relationship("Executes business logic via") >> accounts_service
        update_account_command >> Relationship("Executes business logic via") >> accounts_service
        deactivate_account_command >> Relationship("Executes business logic via") >> accounts_service
        verify_account_command >> Relationship("Executes business logic via") >> accounts_service

        # Relationships - Query Side
        accounts_service >> Relationship("Handles") >> get_account_summary_query
        accounts_service >> Relationship("Handles") >> get_account_details_query
        
        get_account_summary_query >> Relationship("Executes business logic via") >> accounts_service
        get_account_details_query >> Relationship("Executes business logic via") >> accounts_service

        # Supporting Services and Event Publishing
        accounts_service >> Relationship("Validates permissions with") >> auth_service
        accounts_service >> Relationship("Reads from/Writes to") >> accounts_db
        accounts_service >> Relationship("Publishes events via") >> event_publisher
        
        event_publisher >> Relationship("Publishes") >> [
            account_created_event, 
            account_updated_event, 
            account_deactivated_event, 
            account_verified_event
        ]
        
        # Event flow within the system
        account_created_event >> Relationship("Sent via") >> internal_event_bus
        account_updated_event >> Relationship("Sent via") >> internal_event_bus
        account_deactivated_event >> Relationship("Sent via") >> internal_event_bus
        account_verified_event >> Relationship("Sent via") >> internal_event_bus
        
        internal_event_bus >> Relationship("Forwards events to") >> external_event_bus

        # CRM System
        with SystemBoundary("CRM System"):
            leads_service_crm = Container(
                "Leads Summary Service",
                ".NET",
                "Stores data related to users from the Administration Concession System"
            )
            
            crm_event_publisher = Container(
                "CRM Event Publisher",
                "ASP.NET Core with RabbitMQ",
                "Publishes events to CRM event bus"
            )
            
            crm_db = Database(
                "Leads Database",
                "MongoDB",
                "Stores lead-related data"
            )
            
            external_event_bus >> Relationship("Forwards user data to") >> leads_service_crm
            leads_service_crm >> Relationship("Stores data in") >> crm_db
            leads_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
