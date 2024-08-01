from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("Internal Statistics Service - Context Diagram", direction="TB"):
    # Define personas
    admin = Person("System Administrator", "Manages the internal statistics service and monitors system health")
    user = Person("Business User", "Utilizes internal statistics for decision-making and reporting")

    # Define system boundaries
    internal_statistics_service = Container(
        "Internal Statistics Service",
        ".NET",
        "Processes and provides internal statistics such as user activity, performance metrics, and system health"
    )

    # Supporting Systems in CRM
    crm_system = System("CRM System", "Central system for managing customer and lead data")
    ml_service = Container("ML Service", "ML.NET", "Provides machine learning-based analytics and predictions")
    leads_service = Container("Leads Service", ".NET", "Manages and tracks lead information within the CRM")

    # Relationships
    admin >> Relationship("Configures and monitors") >> internal_statistics_service
    user >> Relationship("Accesses internal statistics from") >> internal_statistics_service

    internal_statistics_service >> Relationship("Obtains data from") >> [crm_system, ml_service, leads_service]
