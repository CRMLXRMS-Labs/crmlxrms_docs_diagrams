from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("Orders Service - Context Diagram", direction="TB"):
    # Define personas
    crm_admin = Person("CRM Administrator", "Manages the overall CRM system and has full access.")
    concession_admin = Person("Concession Administrator", "Manages the concession and user access.")
    concession_user = Person("Concession User", "Interacts with the concession system with defined permissions.")
    
    # Define system boundaries
    concession_system = System("Administration Concession System", "Manages concessions and user access")
    
    orders_service = Container(
        "Orders Service",
        ".NET",
        "Manages and provides information related to orders"
    )
    
    auth_service = Container(
        "Authorization Microservice",
        "ASP.NET Core",
        "Handles user authentication and authorization"
    )
    
    crm_system = System("CRM System", "Manages customer relationships and service platform users")
    
    leads_service_crm = Container(
        "Leads Summary Service",
        ".NET",
        "Stores data related to users from the Administration Concession System"
    )

    # Relationships for CRM Administrator
    crm_admin >> Relationship("Monitors and configures") >> concession_system
    crm_admin >> Relationship("Requests order data") >> orders_service
    orders_service >> Relationship("Provides order summary to") >> crm_admin

    # Relationships for Concession Administrator
    concession_admin >> Relationship("Manages and configures access") >> concession_system
    concession_admin >> Relationship("Requests order summary") >> orders_service
    orders_service >> Relationship("Provides order summary to") >> concession_admin
    
    # Relationships for Concession User
    concession_user >> Relationship("Requests order summary with limited access") >> orders_service
    orders_service >> Relationship("Validates permissions with") >> auth_service
    auth_service >> Relationship("Validates user authentication") >> orders_service
    orders_service >> Relationship("Provides order summary to") >> concession_user

    # Integration relationships
    concession_system >> Relationship("Integrates with") >> orders_service
    concession_system >> Relationship("Shares relevant order data with") >> crm_system
    crm_system >> Relationship("Stores user data in") >> leads_service_crm
