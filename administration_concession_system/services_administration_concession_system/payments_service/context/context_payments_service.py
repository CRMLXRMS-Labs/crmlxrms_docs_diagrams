from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("Payments Service - Context Diagram", direction="TB"):
    # Define personas
    crm_admin = Person("CRM CS Administrator", "Manages the overall concession system (user from crm group) and has full access.")
    concession_admin = Person("Concession Administrator", "Manages the concession and user access.")
    concession_user = Person("Concession User", "Interacts with the concession system with defined permissions.")
    
    # Define system boundaries
    concession_system = System("Administration Concession System", "Manages concessions, user access, and payments")
    
    payments_service = Container(
        "Payments Service",
        ".NET",
        "Manages and processes payments within the concession system"
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
        "Handles and stores payment-related data from the Administration Concession System"
    )

    facturation_service_crm = Container(
        "Facturation Service",
        ".NET",
        "Manages invoicing and billing for payments from the Administration Concession System"
    )

    orders_service_crm = Container(
        "Orders Service (CRM)",
        ".NET",
        "Handles and stores order-related payment data from the Administration Concession System"
    )

    # Relationships for CRM Administrator
    crm_admin >> Relationship("Monitors and configures") >> concession_system
    crm_admin >> Relationship("Requests payment data") >> payments_service
    payments_service >> Relationship("Provides payment summary to") >> crm_admin

    # Relationships for Concession Administrator
    concession_admin >> Relationship("Manages and configures access") >> concession_system
    concession_admin >> Relationship("Requests payment summary") >> payments_service
    payments_service >> Relationship("Provides payment summary to") >> concession_admin
    
    # Relationships for Concession User
    concession_user >> Relationship("Requests payment summary with limited access") >> payments_service
    payments_service >> Relationship("Validates permissions with") >> auth_service
    auth_service >> Relationship("Validates user authentication") >> payments_service
    payments_service >> Relationship("Provides payment summary to") >> concession_user

    # Integration relationships
    concession_system >> Relationship("Integrates with") >> payments_service
    payments_service >> Relationship("Shares payment data with") >> crm_system
    crm_system >> Relationship("Processes and stores payment data in") >> [leads_service_crm, facturation_service_crm, orders_service_crm]
