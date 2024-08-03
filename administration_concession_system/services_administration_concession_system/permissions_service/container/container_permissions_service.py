from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Permissions Summary Service - Container Diagram", direction="TB"):
    with SystemBoundary("Administration Concession System"):
        
        # Permissions Summary Service
        permissions_service = Container(
            "Permissions Summary Service",
            ".NET",
            "Manages and provides information about user permissions, including user groups"
        )
        
        # Command Side (CQRS)
        with SystemBoundary("Command Side"):
            create_permissions_command = Container(
                "CreatePermissionsCommand",
                "Command",
                "Handles requests to create new permissions"
            )

            update_permissions_command = Container(
                "UpdatePermissionsCommand",
                "Command",
                "Handles requests to update user permissions"
            )

            deactivate_permissions_command = Container(
                "DeactivatePermissionsCommand",
                "Command",
                "Handles requests to deactivate user permissions"
            )

            create_group_command = Container(
                "CreateGroupCommand",
                "Command",
                "Handles requests to create a new user group with specific permissions"
            )
            
            update_group_command = Container(
                "UpdateGroupCommand",
                "Command",
                "Handles requests to update user group permissions"
            )
            
            deactivate_group_command = Container(
                "DeactivateGroupCommand",
                "Command",
                "Handles requests to deactivate a user group"
            )
        
        # Query Side (CQRS)
        with SystemBoundary("Query Side"):
            get_permissions_summary_query = Container(
                "GetPermissionsSummaryQuery",
                "Query",
                "Fetches a summary of user permissions"
            )

            get_permissions_details_query = Container(
                "GetPermissionsDetailsQuery",
                "Query",
                "Fetches detailed permission information"
            )
            
            get_group_summary_query = Container(
                "GetGroupSummaryQuery",
                "Query",
                "Fetches a summary of user groups and their permissions"
            )

            get_group_details_query = Container(
                "GetGroupDetailsQuery",
                "Query",
                "Fetches detailed group information"
            )

        # Domain Events
        with SystemBoundary("Events"):
            permissions_created_event = Container(
                "PermissionsCreatedEvent",
                "Event",
                "Published when new permissions are created"
            )

            permissions_updated_event = Container(
                "PermissionsUpdatedEvent",
                "Event",
                "Published when permissions are updated"
            )
            
            permissions_deactivated_event = Container(
                "PermissionsDeactivatedEvent",
                "Event",
                "Published when permissions are deactivated"
            )

            group_created_event = Container(
                "GroupCreatedEvent",
                "Event",
                "Published when a new user group is created"
            )

            group_updated_event = Container(
                "GroupUpdatedEvent",
                "Event",
                "Published when a user group is updated"
            )

            group_deactivated_event = Container(
                "GroupDeactivatedEvent",
                "Event",
                "Published when a user group is deactivated"
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
        permissions_db = Database(
            "Permissions Database",
            "MongoDB",
            "Stores permissions-related data, including user groups"
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
        permissions_service >> Relationship("Handles") >> create_permissions_command
        permissions_service >> Relationship("Handles") >> update_permissions_command
        permissions_service >> Relationship("Handles") >> deactivate_permissions_command
        permissions_service >> Relationship("Handles") >> create_group_command
        permissions_service >> Relationship("Handles") >> update_group_command
        permissions_service >> Relationship("Handles") >> deactivate_group_command
        
        create_permissions_command >> Relationship("Executes business logic via") >> permissions_service
        update_permissions_command >> Relationship("Executes business logic via") >> permissions_service
        deactivate_permissions_command >> Relationship("Executes business logic via") >> permissions_service
        create_group_command >> Relationship("Executes business logic via") >> permissions_service
        update_group_command >> Relationship("Executes business logic via") >> permissions_service
        deactivate_group_command >> Relationship("Executes business logic via") >> permissions_service

        # Relationships - Query Side
        permissions_service >> Relationship("Handles") >> get_permissions_summary_query
        permissions_service >> Relationship("Handles") >> get_permissions_details_query
        permissions_service >> Relationship("Handles") >> get_group_summary_query
        permissions_service >> Relationship("Handles") >> get_group_details_query
        
        get_permissions_summary_query >> Relationship("Executes business logic via") >> permissions_service
        get_permissions_details_query >> Relationship("Executes business logic via") >> permissions_service
        get_group_summary_query >> Relationship("Executes business logic via") >> permissions_service
        get_group_details_query >> Relationship("Executes business logic via") >> permissions_service

        # Supporting Services and Event Publishing
        permissions_service >> Relationship("Validates permissions with") >> auth_service
        permissions_service >> Relationship("Reads from/Writes to") >> permissions_db
        permissions_service >> Relationship("Publishes events via") >> event_publisher
        
        event_publisher >> Relationship("Publishes") >> [
            permissions_created_event, 
            permissions_updated_event, 
            permissions_deactivated_event,
            group_created_event,
            group_updated_event,
            group_deactivated_event
        ]
        
        # Event flow within the system
        permissions_created_event >> Relationship("Sent via") >> internal_event_bus
        permissions_updated_event >> Relationship("Sent via") >> internal_event_bus
        permissions_deactivated_event >> Relationship("Sent via") >> internal_event_bus
        group_created_event >> Relationship("Sent via") >> internal_event_bus
        group_updated_event >> Relationship("Sent via") >> internal_event_bus
        group_deactivated_event >> Relationship("Sent via") >> internal_event_bus
        
        internal_event_bus >> Relationship("Forwards events to") >> external_event_bus

        # CRM System
        with SystemBoundary("CRM System"):
            leads_service_crm = Container(
                "Leads Summary Service",
                ".NET",
                "Stores data related to users from the Administration Concession System"
            )

            tasks_summary_service_crm = Container(
                "Tasks Summary Service",
                ".NET",
                "Stores and manages task-related data from the Administration Concession System"
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

            crm_db_tasks = Database(
                "Tasks Database",
                "MongoDB",
                "Stores task-related data"
            )
            
            external_event_bus >> Relationship("Forwards permission and group data to") >> [leads_service_crm, tasks_summary_service_crm]
            leads_service_crm >> Relationship("Stores data in") >> crm_db_leads
            tasks_summary_service_crm >> Relationship("Stores data in") >> crm_db_tasks
            leads_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
            tasks_summary_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
