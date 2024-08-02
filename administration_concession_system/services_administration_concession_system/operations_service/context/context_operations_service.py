from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("Operation gRPC Service - Context Diagram", direction="TB"):
    # Define personas
    admin = Person("Admin of Admin Concession System", "Oversees all operations performed by users")
    crm_admin = Person("CRM Administrator", "Manages CRM system and monitors data received from the Operation gRPC service")
    user = Person("User", "Performs operations and views data through the Admin Concession System")

    # Define system boundaries
    operation_grpc_service = Container(
        "Operation gRPC Service",
        "gRPC",
        "Handles all user operations and communicates with the CRM system"
    )

    # Supporting Systems
    admin_concession_system = System("Administration Concession System", "Manages user interactions and data processing")
    crm_system = System("CRM System", "Manages customer data and statistics, interacting with the Operation gRPC Service")
    external_operations_service = Container("External Operations Service", ".NET", "Handles external operations and integrates data from Operation gRPC Service")
    
    # Relationships
    user >> Relationship("Performs operations through") >> admin_concession_system
    admin_concession_system >> Relationship("Translates operations to") >> operation_grpc_service
    operation_grpc_service >> Relationship("Reports operations to") >> admin
    operation_grpc_service >> Relationship("Sends operational data to") >> external_operations_service
    external_operations_service >> Relationship("Integrates and processes data with") >> crm_system
    crm_system >> Relationship("Provides statistical and processed data to") >> admin_concession_system
    crm_admin >> Relationship("Monitors and configures services via") >> crm_system
