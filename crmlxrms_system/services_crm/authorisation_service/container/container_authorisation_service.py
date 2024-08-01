from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Authorization Microservice - Container Diagram", direction="TB"):
    with SystemBoundary("CRM System"):
        auth_service = Container(
            "Authorization Microservice",
            "ASP.NET Core",
            "Handles authentication and authorization"
        )
        
        auth_db = Database("Auth Database", "MongoDB", "Stores user credentials and authorization data")
        
        internal_event_bus = Container(
            "Internal Event Bus",
            "RabbitMQ",
            "Handles internal communication within the CRM system"
        )
        
        external_event_bus = Container(
            "External Event Bus",
            "RabbitMQ",
            "Handles external communication with other systems"
        )
        
        commands = Container(
            "Commands",
            "CQRS Commands",
            "Handles commands such as UserLoginCommand, UserLogoutCommand"
        )
        
        queries = Container(
            "Queries",
            "CQRS Queries",
            "Handles queries such as GetUserPermissionsQuery"
        )
    
    auth_service >> Relationship("Writes to/Reads from") >> auth_db
    auth_service >> Relationship("Handles") >> [commands, queries]
    auth_service >> Relationship("Publishes events to") >> internal_event_bus
    internal_event_bus >> Relationship("Forwards events to") >> external_event_bus
