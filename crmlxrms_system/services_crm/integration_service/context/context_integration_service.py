from diagrams import Diagram
from diagrams.c4 import Person, System, Relationship

with Diagram("CRM Integration Service - Context Diagram", direction="TB"):
    # External users and systems
    client_app = System("Client Application", "Receives integrated data from CRM")
    crm_user = Person("CRM User", "Manages and monitors CRM integrations")
    
    # CRM System
    crm_system = System("CRM System", "Main CRM system managing customer data")
    
    # Integration Service
    integration_service = System("CRM Integration Service", "Handles data orders and integration with external systems")
    
    # Orders Service
    orders_service = System("Orders Service", "Manages and processes order data within CRM")
    
    # Relationships
    crm_user >> Relationship("Monitors and manages integrations via") >> crm_system
    orders_service >> Relationship("Provides orders data to") >> integration_service
    integration_service >> Relationship("Integrates and sends data to") >> client_app
