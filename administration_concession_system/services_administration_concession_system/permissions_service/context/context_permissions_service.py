from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("Permissions Summary Service - Context Diagram", direction="TB"):
    # Define the personas
    crm_admin = Person("CRM CS Administrator", "Manages the overall concession system (user from crm group) and has full access.")
    concession_admin = Person("Concession Administrator", "Manages the concession and user access.")
    concession_user = Person("Concession User", "Interacts with the concession system with defined permissions.")
    
    # Define the system boundaries
    concession_system = System("Administration Concession System", "Manages concessions and user access")
    
    permissions_service = Container(
        "Permissions Summary Service",
        ".NET",
        "Manages and provides information about user permissions"
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
    
    tasks_service_crm = Container(
        "Tasks Summary Service",
        ".NET",
        "Stores data related to tasks from the Administration Concession System"
    )

    # Relationships for CRM Administrator
    crm_admin >> Relationship("Monitors and configures") >> concession_system
    crm_admin >> Relationship("Requests permission data") >> permissions_service
    permissions_service >> Relationship("Provides permission summary to") >> crm_admin

    # Relationships for Concession Administrator
    concession_admin >> Relationship("Manages and configures access") >> concession_system
    concession_admin >> Relationship("Requests permission summary") >> permissions_service
    permissions_service >> Relationship("Provides permission summary to") >> concession_admin
    
    # Relationships for Concession User
    concession_user >> Relationship("Requests permission summary with limited access") >> permissions_service
    permissions_service >> Relationship("Validates permissions with") >> auth_service
    auth_service >> Relationship("Validates user authentication") >> permissions_service
    permissions_service >> Relationship("Provides permission summary to") >> concession_user

    # Integration relationships
    concession_system >> Relationship("Integrates with") >> permissions_service
    concession_system >> Relationship("Shares relevant permission data with") >> crm_system
    crm_system >> Relationship("Stores user data in") >> leads_service_crm
    crm_system >> Relationship("Stores task data in") >> tasks_service_crm
