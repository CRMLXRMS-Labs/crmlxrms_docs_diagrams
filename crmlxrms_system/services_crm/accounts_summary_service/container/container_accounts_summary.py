from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("Accounts Summary Service - Container Diagram", direction="TB"):
    with SystemBoundary("CRM System"):
        accounts_service = Container(
            "Accounts Summary Service",
            ".NET Core",
            "Provides summary of user accounts"
        )
        
        accounts_db = Database("Accounts Database", "MongoDB", "Stores account data")
        
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
            "Handles commands such as UpdateAccountSummaryCommand"
        )
        
        queries = Container(
            "Queries",
            "CQRS Queries",
            "Handles queries such as GetAccountSummaryQuery"
        )
    
    accounts_service >> Relationship("Reads from") >> accounts_db
    accounts_service >> Relationship("Handles") >> [commands, queries]
    accounts_service >> Relationship("Publishes events to") >> internal_event_bus
    internal_event_bus >> Relationship("Forwards events to") >> external_event_bus
