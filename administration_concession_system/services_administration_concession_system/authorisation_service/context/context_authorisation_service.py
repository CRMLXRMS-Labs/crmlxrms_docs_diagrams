from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("Authorization Microservice - Context Diagram", direction="TB"):
    user = Person("CRM User", "Interacts with the CRM System")
    
    concession_system = System("Administration Concession System", "Manages concessions and user access")
    
    authorization_service = Container(
        "Authorization Microservice",
        "ASP.NET Core",
        "Handles user authentication and authorization"
    )
    
    crm_system = System("CRM System", "Manages customer relationships and service platform users")
    
    leads_service_crm = Container(
        "Leads Summary Service",
        ".NET",
        "Stores data of users from the Administration Concession System"
    )
    
    user >> Relationship("Requests access") >> concession_system
    concession_system >> Relationship("Delegates authentication to") >> authorization_service
    authorization_service >> Relationship("Sends authentication events to") >> concession_system
    
    concession_system >> Relationship("Forwards sign-in events to") >> crm_system
    crm_system << Relationship("Stores user data in") << leads_service_crm
