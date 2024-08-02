from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("CRM External Statistics Service - Context Diagram", direction="TB"):
    # Define personas
    crm_user = Person("CRM User", "Utilizes the CRM system to make data-driven decisions")

    # Define system boundaries
    crm_system = System(
        "CRM System",
        "Manages customer relations, statistics, and decision-making processes"
    )
    
    external_statistics_service = Container(
        "External Statistics Service",
        ".NET",
        "Generates statistical analyses, hypotheses, and risk estimations based on CRM data"
    )
    
    integration_service = Container(
        "CRM Integration Service",
        ".NET",
        "Processes data from external sources and provides it to other CRM services"
    )
    
    ml_service = Container(
        "ML Service",
        ".NET ML",
        "Provides predictive analytics and data cleansing"
    )
    
    crm_user >> Relationship("Uses") >> crm_system
    crm_system >> Relationship("Provides processed data to") >> external_statistics_service
    external_statistics_service >> Relationship("Generates statistical features and insights for") >> crm_user
    
    external_statistics_service >> Relationship("Fetches processed data from") >> integration_service
    external_statistics_service >> Relationship("Fetches insights from") >> ml_service
