from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("External Statistics Service - Context Diagram", direction="TB"):
    # Define personas
    crm_admin = Person("CRM CS Administrator", "Manages the overall concession system (user from CRM group) and has full access.")
    concession_admin = Person("Concession Administrator", "Manages the concession and user access.")
    concession_user = Person("Concession User", "Interacts with the concession system with defined permissions.")
    
    # Define system boundaries
    concession_system = System("Administration Concession System", "Manages concessions and user access")
    
    external_statistics_service = Container(
        "External Statistics Service",
        ".NET",
        "Provides external statistics and analytics"
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
        "Handles and stores data related to statistics from the Administration Concession System"
    )

    orders_service_crm = Container(
        "Orders Service (CRM)",
        ".NET",
        "Handles and stores order-related data from the Administration Concession System"
    )

    facturation_service_crm = Container(
        "Facturation Service (CRM)",
        ".NET",
        "Handles invoicing and billing data related to statistics from the Administration Concession System"
    )

    # Relationships for CRM Administrator
    crm_admin >> Relationship("Monitors and configures") >> concession_system
    crm_admin >> Relationship("Requests statistics data") >> external_statistics_service
    external_statistics_service >> Relationship("Provides statistics summary to") >> crm_admin

    # Relationships for Concession Administrator
    concession_admin >> Relationship("Manages and configures access") >> concession_system
    concession_admin >> Relationship("Requests statistics summary") >> external_statistics_service
    external_statistics_service >> Relationship("Provides statistics summary to") >> concession_admin
    
    # Relationships for Concession User
    concession_user >> Relationship("Requests statistics summary with limited access") >> external_statistics_service
    external_statistics_service >> Relationship("Validates permissions with") >> auth_service
    auth_service >> Relationship("Validates user authentication") >> external_statistics_service
    external_statistics_service >> Relationship("Provides statistics summary to") >> concession_user

    # Integration relationships
    concession_system >> Relationship("Integrates with") >> external_statistics_service
    external_statistics_service >> Relationship("Shares statistics data with") >> crm_system
    crm_system >> Relationship("Processes and stores statistics data in") >> [leads_service_crm, orders_service_crm, facturation_service_crm]
