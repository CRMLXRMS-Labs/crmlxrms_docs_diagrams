from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("CRM External Statistics Service - Container Diagram", direction="TB"):
    with SystemBoundary("CRM System"):
        # Integration Service and Database
        integration_service = Container(
            "CRM Integration Service",
            ".NET",
            "Handles integration-related data and processes it for use by other CRM services"
        )
        
        integration_db = Database(
            "Integration Database",
            "MongoDB",
            "Stores processed data from the integration service"
        )
        
        # ML Service and Database
        ml_service = Container(
            "ML Service",
            ".NET ML",
            "Provides machine learning insights and predictions"
        )
        
        ml_db = Database(
            "ML Database",
            "MongoDB",
            "Stores ML models and predictions"
        )
        
        # External Statistics Service and Database
        external_statistics_service = Container(
            "External Statistics Service",
            ".NET",
            "Generates statistical analyses, hypotheses, and risk estimations"
        )
        
        statistics_db = Database(
            "Statistics Database",
            "MongoDB",
            "Stores statistical analyses, hypotheses, and decision-making data"
        )
        
        # External Client Application
        client_app = Container(
            "Client Application",
            "Web Application",
            "Receives statistical insights and analyses"
        )
        
        # Relationships
        integration_service >> Relationship("Fetches and processes data from") >> integration_db
        ml_service >> Relationship("Fetches models and predictions from") >> ml_db
        
        external_statistics_service >> Relationship("Fetches processed data from") >> integration_service
        external_statistics_service >> Relationship("Fetches predictions and insights from") >> ml_service
        external_statistics_service >> Relationship("Stores statistical analyses and decisions in") >> statistics_db
        
        external_statistics_service >> Relationship("Sends statistical insights to") >> client_app
