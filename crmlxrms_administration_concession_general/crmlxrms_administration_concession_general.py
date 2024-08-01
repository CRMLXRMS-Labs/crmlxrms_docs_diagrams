from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
    "nodesep": "3.0",
    "ranksep": "4.0"
}

with Diagram("Enhanced Schema for Administration and CRM Systems", direction="TB", graph_attr=graph_attr):
    user_admin = Person(name="Administration User", description="User interacting with the Administration system.")
    user_crm = Person(name="CRM User", description="User interacting with the CRM system.")
    
    with SystemBoundary("Administration Concession System"):
        api_gateway_admin = Container(
            name="API Gateway Interface",
            technology="Spring Boot",
            description="Serves as an entry point for API requests."
        )
        
        fabio_load_balancer_admin = Container(
            name="Fabio Load Balancer",
            technology="HAProxy",
            description="Balances the load among HTTP clients using Consul."
        )
        
        event_bus_admin = Container(
            name="Event Bus",
            technology="RabbitMQ",
            description="Handles the events within the system."
        )
        
        # Dual Subscription Service in Administration System
        dual_subscription_service_admin = Container(
            name="Dual Subscription Service",
            technology="Custom",
            description="Subscribes to CRM events and republishes to the Administration event bus."
        )
        
        # Define Administration Services
        accounts_summary_service_admin = Container(
            name="Accounts Summary Service",
            technology=".NET",
            description="Provides users with a summary of their accounts."
        )
        
        leads_summary_service_admin = Container(
            name="Leads Summary Service",
            technology=".NET",
            description="Provides users with a summary of their leads."
        )
        
        tasks_summary_service_admin = Container(
            name="Tasks Summary Service",
            technology=".NET",
            description="Provides users with a summary of their tasks."
        )
        
        permissions_service_admin = Container(
            name="Permissions Service",
            technology=".NET",
            description="Manages permissions and access control."
        )
        
        orders_service_admin = Container(
            name="Orders Service",
            technology=".NET",
            description="Manages and provides information related to orders."
        )
        
        internal_statistics_service_admin = Container(
            name="Statistics Service (internal)",
            technology=".NET",
            description="Provides internal statistics and analytics."
        )
        
        external_statistics_service_admin = Container(
            name="Statistics Service (external)",
            technology=".NET",
            description="Provides external statistics and analytics."
        )
        
        ml_service_admin = Container(
            name="ML Service",
            technology=".NET",
            description="Provides machine learning-based analytics and predictions."
        )
        
        payment_service_admin = Container(
            name="Payment Service",
            technology=".NET",
            description="Manages payment processing and related data."
        )
        
        external_services_admin = Container(
            name="Operation External Services",
            technology=".NET",
            description="Manages interactions with external operational services."
        )
        
        # Define Administration Databases
        accounts_db_admin = Database(
            name="Accounts Database",
            technology="MongoDB",
            description="Stores account-related data."
        )
        
        leads_db_admin = Database(
            name="Leads Database",
            technology="MongoDB",
            description="Stores lead-related data."
        )
        
        tasks_db_admin = Database(
            name="Tasks Database",
            technology="MongoDB",
            description="Stores task-related data."
        )
        
        permissions_db_admin = Database(
            name="Permissions Database",
            technology="MongoDB",
            description="Stores permissions-related data."
        )
        
        orders_db_admin = Database(
            name="Orders Database",
            technology="MongoDB",
            description="Stores order-related data."
        )
        
        internal_statistics_db_admin = Database(
            name="Internal Statistics Database",
            technology="MongoDB",
            description="Stores internal statistics data."
        )
        
        external_statistics_db_admin = Database(
            name="External Statistics Database",
            technology="MongoDB",
            description="Stores external statistics data."
        )
        
        ml_db_admin = Database(
            name="ML Database",
            technology="MongoDB",
            description="Stores machine learning-related data."
        )
        
        payments_db_admin = Database(
            name="Payments Database",
            technology="MongoDB",
            description="Stores payment-related data."
        )
        
    with SystemBoundary("CRM/LXRMS System"):
        api_gateway_crm = Container(
            name="API Gateway Interface",
            technology="Spring Boot",
            description="Serves as an entry point for API requests."
        )
        
        fabio_load_balancer_crm = Container(
            name="Fabio Load Balancer",
            technology="HAProxy",
            description="Balances the load among HTTP clients using Consul."
        )
        
        event_bus_crm = Container(
            name="Event Bus",
            technology="RabbitMQ",
            description="Handles the events within the system."
        )
        
        # Dual Subscription Service in CRM System
        dual_subscription_service_crm = Container(
            name="Dual Subscription Service",
            technology="Custom",
            description="Subscribes to Administration events and republishes to the CRM event bus."
        )
        
        # Event Bus Bridging Service
        event_bus_bridge = Container(
            name="Event Bus Bridge",
            technology="Custom",
            description="Bridges events between the Administration and CRM event buses."
        )
        
        # Define CRM Services
        accounts_summary_service_crm = Container(
            name="Accounts Summary Service",
            technology=".NET",
            description="Provides users with a summary of their accounts."
        )
        
        leads_summary_service_crm = Container(
            name="Leads Summary Service",
            technology=".NET",
            description="Provides users with a summary of their leads."
        )
        
        tasks_summary_service_crm = Container(
            name="Tasks Summary Service",
            technology=".NET",
            description="Provides users with a summary of their tasks."
        )
        
        integration_service_crm = Container(
            name="Integration Service",
            technology=".NET",
            description="Provides users with integration-related data and services."
        )
        
        permissions_service_crm = Container(
            name="Permissions Service",
            technology=".NET",
            description="Manages permissions and access control."
        )
        
        orders_service_crm = Container(
            name="Orders Service",
            technology=".NET",
            description="Manages and provides information related to orders."
        )
        
        internal_statistics_service_crm = Container(
            name="Statistics Service (internal)",
            technology=".NET",
            description="Provides internal statistics and analytics."
        )
        
        external_statistics_service_crm = Container(
            name="Statistics Service (external)",
            technology=".NET",
            description="Provides external statistics and analytics."
        )
        
        ml_service_crm = Container(
            name="ML Service",
            technology=".NET",
            description="Provides machine learning-based analytics and predictions."
        )
        
        payment_service_crm = Container(
            name="Payment Service",
            technology=".NET",
            description="Manages payment processing and related data."
        )
        
        facturation_service_crm = Container(
            name="Facturation System Service",
            technology=".NET",
            description="Provides factureation processing services."
        )
        
        authorization_microservice_crm = Container(
            name="Authorization Microservice",
            technology=".Net",
            description="Manages user authentication and authorization."
        )
        
        external_services_crm = Container(
            name="Operation External Services",
            technology=".NET",
            description="Manages interactions with external operational services."
        )
        
        # Define CRM Databases
        accounts_db_crm = Database(
            name="Accounts Database",
            technology="MongoDB",
            description="Stores account-related data."
        )
        
        leads_db_crm = Database(
            name="Leads Database",
            technology="MongoDB",
            description="Stores lead-related data."
        )
        
        tasks_db_crm = Database(
            name="Tasks Database",
            technology="MongoDB",
            description="Stores task-related data."
        )
        
        integration_db_crm = Database(
            name="Integration Database",
            technology="MongoDB",
            description="Stores integration-related data."
        )
        
        permissions_db_crm = Database(
            name="Permissions Database",
            technology="MongoDB",
            description="Stores permissions-related data."
        )
        
        orders_db_crm = Database(
            name="Orders Database",
            technology="MongoDB",
            description="Stores order-related data."
        )
        
        internal_statistics_db_crm = Database(
            name="Internal Statistics Database",
            technology="MongoDB",
            description="Stores internal statistics data."
        )
        
        external_statistics_db_crm = Database(
            name="External Statistics Database",
            technology="MongoDB",
            description="Stores external statistics data."
        )
        
        ml_db_crm = Database(
            name="ML Database",
            technology="MongoDB",
            description="Stores machine learning-related data."
        )
        
        payments_db_crm = Database(
            name="Payments Database",
            technology="MongoDB",
            description="Stores payment-related data."
        )
        
        fortification_db_crm = Database(
            name="Fortification Database",
            technology="MongoDB",
            description="Stores fortification-related data."
        )
        
        auth_db_crm = Database(
            name="Authorization Database",
            technology="MongoDB",
            description="Stores authorization keys and data."
        )
    
    # Define Relationships for Administration System
    user_admin >> Relationship("Uses") >> api_gateway_admin
    api_gateway_admin >> Relationship("Routes requests through") >> fabio_load_balancer_admin
    fabio_load_balancer_admin >> Relationship("Forwards requests to") >> [
        accounts_summary_service_admin,
        leads_summary_service_admin,
        tasks_summary_service_admin,
        permissions_service_admin,
        orders_service_admin,
        internal_statistics_service_admin,
        external_statistics_service_admin,
        ml_service_admin,
        payment_service_admin
    ]
    
    accounts_summary_service_admin >> Relationship("Stores data in") >> accounts_db_admin
    leads_summary_service_admin >> Relationship("Stores data in") >> leads_db_admin
    tasks_summary_service_admin >> Relationship("Stores data in") >> tasks_db_admin
    permissions_service_admin >> Relationship("Stores data in") >> permissions_db_admin
    orders_service_admin >> Relationship("Stores data in") >> orders_db_admin
    internal_statistics_service_admin >> Relationship("Stores data in") >> internal_statistics_db_admin
    external_statistics_service_admin >> Relationship("Stores data in") >> external_statistics_db_admin
    ml_service_admin >> Relationship("Stores data in") >> ml_db_admin
    payment_service_admin >> Relationship("Stores data in") >> payments_db_admin
    accounts_summary_service_admin << Relationship("Publishes events to") << event_bus_admin
    leads_summary_service_admin << Relationship("Publishes events to") << event_bus_admin
    tasks_summary_service_admin << Relationship("Publishes events to") << event_bus_admin
    
    # Define Relationships for CRM System
    user_crm >> Relationship("Uses") >> api_gateway_crm
    api_gateway_crm >> Relationship("Routes requests through") >> fabio_load_balancer_crm
    fabio_load_balancer_crm >> Relationship("Forwards requests to") >> [
        accounts_summary_service_crm,
        leads_summary_service_crm,
        tasks_summary_service_crm,
        integration_service_crm,
        permissions_service_crm,
        orders_service_crm,
        internal_statistics_service_crm,
        external_statistics_service_crm,
        ml_service_crm,
        payment_service_crm,
        facturation_service_crm,
        authorization_microservice_crm
    ]
    
    accounts_summary_service_crm >> Relationship("Stores data in") >> accounts_db_crm
    leads_summary_service_crm >> Relationship("Stores data in") >> leads_db_crm
    tasks_summary_service_crm >> Relationship("Stores data in") >> tasks_db_crm
    integration_service_crm >> Relationship("Stores data in") >> integration_db_crm
    permissions_service_crm >> Relationship("Stores data in") >> permissions_db_crm
    orders_service_crm >> Relationship("Stores data in") >> orders_db_crm
    internal_statistics_service_crm >> Relationship("Stores data in") >> internal_statistics_db_crm
    external_statistics_service_crm >> Relationship("Stores data in") >> external_statistics_db_crm
    ml_service_crm >> Relationship("Stores data in") >> ml_db_crm
    payment_service_crm >> Relationship("Stores data in") >> payments_db_crm
    facturation_service_crm >> Relationship("Stores data in") >> fortification_db_crm
    authorization_microservice_crm >> Relationship("Stores data in") >> auth_db_crm
    accounts_summary_service_crm << Relationship("Publishes events to") << event_bus_crm
    leads_summary_service_crm << Relationship("Publishes events to") << event_bus_crm
    tasks_summary_service_crm << Relationship("Publishes events to") << event_bus_crm
    
    # Operation External Services Communication
    external_services_admin >> Relationship("Communicates with") >> external_services_crm
    
    # Dual Subscription Relationships
    dual_subscription_service_admin >> Relationship("Subscribes to and republishes CRM events to Admin Event Bus") >> event_bus_admin
    dual_subscription_service_crm >> Relationship("Subscribes to and republishes Admin events to CRM Event Bus") >> event_bus_crm
    
    # Event Bus Bridging Relationship
    event_bus_bridge >> Relationship("Bridges events between Administration and CRM Event Buses") >> [event_bus_admin, event_bus_crm]
    
    # Federated Event Bus Relationships
    event_bus_admin << Relationship("Replicates necessary topics and queues") >> event_bus_crm
    event_bus_crm << Relationship("Replicates necessary topics and queues") >> event_bus_admin
