from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("External Statistics Service - Context Diagram", direction="TB"):
    # Define personas
    client_admin = Person("Client Administrator", "Manages client-side application settings and integration")
    crm_admin = Person("CRM Administrator", "Oversees CRM system and manages data processing")
    concession_admin = Person("Concession Administrator", "Manages access to statistics in the administration concession system")

    # Define system boundaries
    external_statistics_service = Container(
        "External Statistics Service",
        ".NET",
        "Provides client-specific statistics like behavior analysis and risk assessment"
    )

    # CRM System providing data
    crm_system = System("CRM System", "Centralized Customer Relationship Management System")
    integration_service = Container("Integration Service", "ASP.NET Core", "Integrates data from various sources")
    ml_service = Container("ML Service", "ML.NET", "Performs machine learning-based analytics")
    facturation_service = Container("Facturation Service", "ASP.NET Core", "Handles invoicing and payment processing")
    external_statistics_service_crm = Container("External Statistics Service (CRM)", "ASP.NET Core", "Generates and processes statistics within CRM")

    # Relationships
    client_admin >> Relationship("Configures data collection for") >> external_statistics_service
    crm_admin >> Relationship("Oversees data processing and analysis in") >> crm_system
    concession_admin >> Relationship("Accesses statistics via") >> external_statistics_service

    crm_system >> Relationship("Processes data through") >> [integration_service, ml_service, facturation_service, external_statistics_service_crm]
    external_statistics_service_crm >> Relationship("Provides pre-processed statistics to") >> external_statistics_service
    external_statistics_service >> Relationship("Presents statistics to") >> concession_admin
