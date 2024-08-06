from diagrams import Diagram
from diagrams.c4 import Person, System, Relationship

with Diagram("Payments CRM Microservice - Context Diagram", direction="TB"):
    # External users and systems
    crm_user = Person("CRM User", "Facilitates transactions and payment processing with Payment Service")
    client_app = System("Client Application", "Receives insights and predictions from CRM")

    # CRM System
    crm_system = System("CRM System", "Main CRM system managing customer data")

    # Payments Service
    payments_service = System("Payments CRM Microservice", "Provides payment processing and payment-related data")

    # Relationships
    crm_user >> Relationship("Utilizes insights from") >> crm_system
    crm_system >> Relationship("Processes payment with") >> payments_service
    crm_system >> Relationship("Provides payment insights and transaction history to") >> client_app
