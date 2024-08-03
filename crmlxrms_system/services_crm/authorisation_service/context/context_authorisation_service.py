from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("Authorization Microservice - Context Diagram", direction="TB"):
    user = Person("CRM User", "Interacts with the CRM system")
    
    crm_system = System("CRM System", "Handles customer relationships")
    
    authorization_service = Container(
        "Authorization Microservice",
        "ASP.NET Core",
        "Handles user authentication and authorization"
    )
    
    user >> Relationship("Requests access") >> crm_system
    crm_system >> Relationship("Delegates auth to") >> authorization_service
