from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
    "nodesep": "1.0",  # increase the space between nodes
    "ranksep": "1.0"   # increase the space between ranks
}

with Diagram("Container Diagram for CRM/LXRMS System", direction="TB", graph_attr=graph_attr):
    user = Person(name="CRM User", description="User interacting with the CRM system.")
    
    with SystemBoundary("CRM System"):
        api_gateway = Container(
            name="API Gateway Interface",
            technology="Spring Boot",
            description="Serves as an entry point for API requests."
        )
        
        fabio_load_balancer = Container(
            name="Fabio Load Balancer",
            technology="HAProxy",
            description="Balances the load among HTTP clients using Consul."
        )
        
        event_bus = Container(
            name="Event Bus",
            technology="RabbitMQ",
            description="Handles the events within the system."
        )
        
        # Define Services
        accounts_summary_service = Container(
            name="Accounts Summary Service",
            technology=".NET",
            description="Provides users with a summary of their accounts."
        )
        
        leads_summary_service = Container(
            name="Leads Summary Service",
            technology=".NET",
            description="Provides users with a summary of their leads."
        )
        
        tasks_summary_service = Container(
            name="Tasks Summary Service",
            technology=".NET",
            description="Provides users with a summary of their tasks."
        )
        
        integration_service = Container(
            name="Integration Service",
            technology=".NET",
            description="Provides users with integration-related data and services."
        )
        
        permissions_service = Container(
            name="Permissions Service",
            technology=".NET",
            description="Manages permissions and access control."
        )
        
        orders_service = Container(
            name="Orders Service",
            technology=".NET",
            description="Manages and provides information related to orders."
        )
        
        internal_statistics_service = Container(
            name="Statistics Service (internal)",
            technology=".NET",
            description="Provides internal statistics and analytics."
        )
        
        external_statistics_service = Container(
            name="Statistics Service (external)",
            technology=".NET",
            description="Provides external statistics and analytics."
        )
        
        ml_service = Container(
            name="ML Service",
            technology=".NET",
            description="Provides machine learning-based analytics and predictions."
        )
        
        payment_service = Container(
            name="Payment Service",
            technology=".NET",
            description="Manages payment processing and related data."
        )
        
        fortification_service = Container(
            name="Fortification System Service",
            technology=".NET",
            description="Provides security and fortification-related services."
        )
        
        authorization_microservice = Container(
            name="Authorization Microservice",
            technology="Spring Boot",
            description="Manages user authentication and authorization."
        )
        
        external_services = Container(
            name="Operation External Services",
            technology=".NET",
            description="Manages interactions with external operational services."
        )
        
        # Define Databases
        accounts_db = Database(
            name="Accounts Database",
            technology="MongoDB",
            description="Stores account-related data."
        )
        
        leads_db = Database(
            name="Leads Database",
            technology="MongoDB",
            description="Stores lead-related data."
        )
        
        tasks_db = Database(
            name="Tasks Database",
            technology="MongoDB",
            description="Stores task-related data."
        )
        
        integration_db = Database(
            name="Integration Database",
            technology="MongoDB",
            description="Stores integration-related data."
        )
        
        permissions_db = Database(
            name="Permissions Database",
            technology="MongoDB",
            description="Stores permissions-related data."
        )
        
        orders_db = Database(
            name="Orders Database",
            technology="MongoDB",
            description="Stores order-related data."
        )
        
        internal_statistics_db = Database(
            name="Internal Statistics Database",
            technology="MongoDB",
            description="Stores internal statistics data."
        )
        
        external_statistics_db = Database(
            name="External Statistics Database",
            technology="MongoDB",
            description="Stores external statistics data."
        )
        
        ml_db = Database(
            name="ML Database",
            technology="MongoDB",
            description="Stores machine learning-related data."
        )
        
        payments_db = Database(
            name="Payments Database",
            technology="MongoDB",
            description="Stores payment-related data."
        )
        
        fortification_db = Database(
            name="Fortification Database",
            technology="MongoDB",
            description="Stores fortification-related data."
        )
        
        auth_db = Database(
            name="Authorization Database",
            technology="MongoDB",
            description="Stores authorization keys and data."
        )
        
    # Define Relationships
    user >> Relationship("Uses") >> api_gateway
    api_gateway >> Relationship("Routes requests through") >> fabio_load_balancer
    fabio_load_balancer >> Relationship("Forwards requests to") >> [
        accounts_summary_service,
        leads_summary_service,
        tasks_summary_service,
        integration_service,
        permissions_service,
        orders_service,
        internal_statistics_service,
        external_statistics_service,
        ml_service,
        payment_service,
        fortification_service,
        authorization_microservice,
        external_services
    ]
    
    accounts_summary_service >> Relationship("Stores data in") >> accounts_db
    leads_summary_service >> Relationship("Stores data in") >> leads_db
    tasks_summary_service >> Relationship("Stores data in") >> tasks_db
    integration_service >> Relationship("Stores data in") >> integration_db
    permissions_service >> Relationship("Stores data in") >> permissions_db
    orders_service >> Relationship("Stores data in") >> orders_db
    internal_statistics_service >> Relationship("Stores data in") >> internal_statistics_db
    external_statistics_service >> Relationship("Stores data in") >> external_statistics_db
    ml_service >> Relationship("Stores data in") >> ml_db
    payment_service >> Relationship("Stores data in") >> payments_db
    fortification_service >> Relationship("Stores data in") >> fortification_db
    authorization_microservice >> Relationship("Stores data in") >> auth_db
    
    # Services sending events to Event Bus
    accounts_summary_service >> Relationship("Sends: AccountCreatedEvent, AccountUpdatedEvent") >> event_bus
    leads_summary_service >> Relationship("Sends: LeadCreatedEvent, LeadUpdatedEvent") >> event_bus
    tasks_summary_service >> Relationship("Sends: TaskCreatedEvent, TaskUpdatedEvent") >> event_bus
    integration_service >> Relationship("Sends: IntegrationDataUpdatedEvent") >> event_bus
    permissions_service >> Relationship("Sends: PermissionGrantedEvent, PermissionRevokedEvent") >> event_bus
    orders_service >> Relationship("Sends: OrderPlacedEvent, OrderCancelledEvent") >> event_bus
    internal_statistics_service >> Relationship("Sends: InternalMetricsUpdatedEvent") >> event_bus
    external_statistics_service >> Relationship("Sends: ExternalMetricsUpdatedEvent") >> event_bus
    ml_service >> Relationship("Sends: PredictionResultEvent") >> event_bus
    payment_service >> Relationship("Sends: PaymentProcessedEvent, PaymentFailedEvent") >> event_bus
    fortification_service >> Relationship("Sends: SecurityAlertEvent, SecurityUpdateEvent") >> event_bus
    authorization_microservice >> Relationship("Sends: UserAuthenticatedEvent, UserAuthorizationUpdatedEvent") >> event_bus
    
    # Services consuming events from Event Bus
    accounts_summary_service << Relationship("Consumes: AccountCreatedEvent, AccountUpdatedEvent") << event_bus
    leads_summary_service << Relationship("Consumes: LeadCreatedEvent, LeadUpdatedEvent") << event_bus
    tasks_summary_service << Relationship("Consumes: TaskCreatedEvent, TaskUpdatedEvent") << event_bus
    integration_service << Relationship("Consumes: IntegrationDataUpdatedEvent") << event_bus
    permissions_service << Relationship("Consumes: PermissionGrantedEvent, PermissionRevokedEvent") << event_bus
    orders_service << Relationship("Consumes: OrderPlacedEvent, OrderCancelledEvent") << event_bus
    internal_statistics_service << Relationship("Consumes: InternalMetricsUpdatedEvent") << event_bus
    external_statistics_service << Relationship("Consumes: ExternalMetricsUpdatedEvent") << event_bus
    ml_service << Relationship("Consumes: PredictionResultEvent") << event_bus
    payment_service << Relationship("Consumes: PaymentProcessedEvent, PaymentFailedEvent") << event_bus
    fortification_service << Relationship("Consumes: SecurityAlertEvent, SecurityUpdateEvent") << event_bus
    authorization_microservice << Relationship("Consumes: UserAuthenticatedEvent, UserAuthorizationUpdatedEvent") << event_bus
