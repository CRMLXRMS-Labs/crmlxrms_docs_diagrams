from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Tasks Summary Service - Container Diagram", direction="TB"):
    with SystemBoundary("Administration Concession System"):
        
        # Tasks Summary Service
        tasks_service = Container(
            "Tasks Summary Service",
            ".NET",
            "Provides users with a summary of their tasks"
        )
        
        # Command Side (CQRS)
        with SystemBoundary("Command Side"):
            update_task_command = Container(
                "UpdateTaskCommand",
                "Command",
                "Handles requests to update task information"
            )

            deactivate_task_command = Container(
                "DeactivateTaskCommand",
                "Command",
                "Handles requests to deactivate a task"
            )
            
            create_task_command = Container(
                "CreateTaskCommand",
                "Command",
                "Handles requests to create a new task"
            )
        
        # Query Side (CQRS)
        with SystemBoundary("Query Side"):
            get_task_summary_query = Container(
                "GetTaskSummaryQuery",
                "Query",
                "Fetches a summary of a user's tasks"
            )

            get_task_details_query = Container(
                "GetTaskDetailsQuery",
                "Query",
                "Fetches detailed task information"
            )

        # Domain Events
        with SystemBoundary("Events"):
            task_created_event = Container(
                "TaskCreatedEvent",
                "Event",
                "Published when a new task is created"
            )

            task_updated_event = Container(
                "TaskUpdatedEvent",
                "Event",
                "Published when a task is updated"
            )
            
            task_deactivated_event = Container(
                "TaskDeactivatedEvent",
                "Event",
                "Published when a task is deactivated"
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
        tasks_db = Database(
            "Tasks Database",
            "MongoDB",
            "Stores task-related data"
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
        tasks_service >> Relationship("Handles") >> create_task_command
        tasks_service >> Relationship("Handles") >> update_task_command
        tasks_service >> Relationship("Handles") >> deactivate_task_command
        
        create_task_command >> Relationship("Executes business logic via") >> tasks_service
        update_task_command >> Relationship("Executes business logic via") >> tasks_service
        deactivate_task_command >> Relationship("Executes business logic via") >> tasks_service

        # Relationships - Query Side
        tasks_service >> Relationship("Handles") >> get_task_summary_query
        tasks_service >> Relationship("Handles") >> get_task_details_query
        
        get_task_summary_query >> Relationship("Executes business logic via") >> tasks_service
        get_task_details_query >> Relationship("Executes business logic via") >> tasks_service

        # Supporting Services and Event Publishing
        tasks_service >> Relationship("Validates permissions with") >> auth_service
        tasks_service >> Relationship("Reads from/Writes to") >> tasks_db
        tasks_service >> Relationship("Publishes events via") >> event_publisher
        
        event_publisher >> Relationship("Publishes") >> [
            task_created_event, 
            task_updated_event, 
            task_deactivated_event
        ]
        
        # Event flow within the system
        task_created_event >> Relationship("Sent via") >> internal_event_bus
        task_updated_event >> Relationship("Sent via") >> internal_event_bus
        task_deactivated_event >> Relationship("Sent via") >> internal_event_bus
        
        internal_event_bus >> Relationship("Forwards events to") >> external_event_bus

        # CRM System
        with SystemBoundary("CRM System"):
            leads_service_crm = Container(
                "Leads Summary Service",
                ".NET",
                "Stores data related to tasks from the Administration Concession System"
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
            
            external_event_bus >> Relationship("Forwards task data to") >> leads_service_crm
            leads_service_crm >> Relationship("Stores data in") >> crm_db
            leads_service_crm >> Relationship("Publishes events via") >> crm_event_publisher
