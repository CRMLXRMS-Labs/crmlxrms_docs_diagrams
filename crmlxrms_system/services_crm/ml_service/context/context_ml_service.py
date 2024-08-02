from diagrams import Diagram
from diagrams.c4 import Person, System, Relationship

with Diagram("ML CRM Microservice - Context Diagram", direction="TB"):
    # External users and systems
    crm_user = Person("CRM User", "Utilizes insights and predictions from ML Service")
    external_data_source = System("External Data Sources", "Provides data for training ML models")
    client_app = System("Client Application", "Receives insights and predictions from CRM")

    # CRM System
    crm_system = System("CRM System", "Main CRM system managing customer data")

    # ML Service
    ml_service = System("ML CRM Microservice", "Provides machine learning insights and predictions")

    # Relationships
    crm_user >> Relationship("Utilizes insights from") >> crm_system
    crm_system >> Relationship("Requests predictions from") >> ml_service
    ml_service >> Relationship("Fetches training data from") >> external_data_source
    crm_system >> Relationship("Sends insights and predictions to") >> client_app
