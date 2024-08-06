from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("CRM Payments Service - Container Diagram", direction="TB"):
    with SystemBoundary("CRM System"):
        # Invoicing Service and Database
        invoicing_service = Container(
            "Invoicing Service",
            ".NET",
            "Handles payment-related data and processes it for invoicing"
        )

        invoicing_db = Database(
            "Invoicing Database",
            "MongoDB",
            "Stores processed data from the invoicing service"
        )

        # Orders and Database
        orders_service = Container(
            "Orders Service",
            ".NET ML",
            "Manages orders withing the CRM system"
        )

        orders_db = Database(
            "Orders Database",
            "MongoDB",
            "Stores order-related data"
        )

        # Payments Service and Database
        payments_service = Container(
            "Payments Service",
            ".NET",
            "Manages payment processing and payment-related data"
        )

        payments_db = Database(
            "Payments Database",
            "MongoDB",
            "Stores payment-related data, including transaction history and payment methods"
        )

        # External Client Application
        client_app = Container(
            "Client Application",
            "Web Application",
            "Provides payment insights and transaction history to clients"
        )

        # Relationships
        invoicing_service >> Relationship("Fetches and processes data from") >> invoicing_db
        orders_service >> Relationship("Fetches and processes data from") >> orders_db

        payments_service >> Relationship("Fetches processed data from") >> invoicing_service
        payments_service >> Relationship("Processes and forwards data to") >> orders_service
        payments_service >> Relationship("Stores payment details and history in") >> payments_db

        payments_service >> Relationship("Shows payment information") >> client_app
