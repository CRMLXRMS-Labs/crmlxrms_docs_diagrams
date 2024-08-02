from diagrams import Diagram
from diagrams.c4 import Container, Database, SystemBoundary, Relationship

with Diagram("CRM Integration Service with Advanced Web Scraper and ML Service - Container Diagram", direction="TB"):
    with SystemBoundary("CRM System"):
        # Orders Service and Database
        orders_service = Container(
            "Orders Service",
            ".NET",
            "Manages and processes orders within the CRM"
        )
        
        orders_db = Database(
            "Orders Database",
            "MongoDB",
            "Stores order-related data"
        )
        
        # Integration Service and Database
        integration_service = Container(
            "CRM Integration Service",
            ".NET",
            "Handles integration-related data, including advanced web scraping"
        )
        
        integration_db = Database(
            "Integration Database",
            "MongoDB",
            "Stores integration-related data, including scraped data"
        )
        
        # Advanced Web Scraper Component
        advanced_web_scraper = Container(
            "Advanced Web Scraper",
            "Python/Selenium",
            "Captures HTML, API requests/responses, and user-provided data"
        )
        
        # Network Traffic Interceptor Component
        network_interceptor = Container(
            "Network Traffic Interceptor",
            "Python/mitmproxy",
            "Intercepts and logs all network traffic, including API calls"
        )
        
        # Data Processor Component
        data_processor = Container(
            "Data Processor",
            ".NET",
            "Processes and cleans captured data before integration"
        )
        
        # ML Service Component
        ml_service = Container(
            "ML Service",
            ".NET ML",
            "Analyzes data to predict user behavior, cleanse data, and personalize experiences"
        )
        
        # External Client Application
        client_app = Container(
            "Client Application",
            "Web Application",
            "Source of user behavior data, receives integrated data from CRM"
        )
        
        # Relationships
        orders_service >> Relationship("Fetches orders data from") >> orders_db
        orders_service >> Relationship("Provides orders data to") >> integration_service
        integration_service >> Relationship("Stores integration data in") >> integration_db
        
        advanced_web_scraper >> Relationship("Scrapes HTML and user-provided data from") >> client_app
        advanced_web_scraper >> Relationship("Sends raw data to") >> data_processor
        
        network_interceptor >> Relationship("Intercepts and logs network traffic from") >> client_app
        network_interceptor >> Relationship("Forwards API requests/responses to") >> data_processor
        
        data_processor >> Relationship("Processes and forwards data to") >> integration_service
        data_processor >> Relationship("Provides processed data to") >> ml_service
        
        ml_service >> Relationship("Analyzes and returns insights to") >> integration_service
        integration_service >> Relationship("Sends integrated data to") >> client_app
