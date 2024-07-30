from diagrams import Diagram, Cluster, Edge
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.storage import PVC
from diagrams.onprem.client import Users

with Diagram("Distributed CRMLXRMS & Administration Concessions Management System", show=False):

    user = Users("Customer")
    
    with Cluster("Internet"):
        dns = Ingress("DNS")

    with Cluster("Banking System"):
        load_balancer = Service("Load Balancer")

        with Cluster("Administration Concession System Services"):
            accounts_summary = Pod("Accounts Summary Service")
            leads_summary = Pod("Leads Summary Service")
            tasks_summary = Pod("Tasks Summary Service")
            permissions = Pod("Permissions Service")
            orders = Pod("Orders Service")
            stats_internal = Pod("Statistics Service (internal)")
            stats_external = Pod("Statistics Service (external)")
            ml_service = Pod("ML Service")
            payment = Pod("Payment Service")

            accounts_db = PVC("Account Summary Data")
            leads_db = PVC("Leads Summary Data")
            tasks_db = PVC("Tasks Summary Data")
            permissions_db = PVC("Permissions Data")
            orders_db = PVC("Orders Data")
            stats_internal_db = PVC("Internal Stats Data")
            stats_external_db = PVC("External Stats Data")
            ml_db = PVC("ML Data")
            payment_db = PVC("Payment Data")

        accounts_summary >> accounts_db
        leads_summary >> leads_db
        tasks_summary >> tasks_db
        permissions >> permissions_db
        orders >> orders_db
        stats_internal >> stats_internal_db
        stats_external >> stats_external_db
        ml_service >> ml_db
        payment >> payment_db

        with Cluster("CRM System Services"):
            crm_accounts_summary = Pod("Accounts Summary Service")
            crm_leads_summary = Pod("Leads Summary Service")
            crm_tasks_summary = Pod("Tasks Summary Service")
            integration = Pod("Integration Service")
            crm_permissions = Pod("Permissions Service")
            crm_orders = Pod("Orders Service")
            crm_stats_internal = Pod("Statistics Service (internal)")
            crm_stats_external = Pod("Statistics Service (external)")
            crm_ml_service = Pod("ML Service")
            crm_payment = Pod("Payment Service")
            fortification = Pod("Fortification System Service")
            mobile_app = Pod("Mobile App")
            api_gateway = Pod("Api Gateway Interface")
            auth_microservice = Pod("Authorization Microservice")
            event_log = Pod("Event Log Instance")
            external_services = Pod("Operation External Services")

            integration_db = PVC("Integration Data")
            payment_db_crm = PVC("Payment Data")
            http_load_balancer = Service("Http Clients Load Balancer")

        crm_accounts_summary >> integration_db
        crm_leads_summary >> integration_db
        crm_tasks_summary >> integration_db
        integration >> integration_db
        crm_permissions >> integration_db
        crm_orders >> integration_db
        crm_stats_internal >> integration_db
        crm_stats_external >> integration_db
        crm_ml_service >> integration_db
        crm_payment >> payment_db_crm
        fortification >> integration_db
        mobile_app >> api_gateway
        auth_microservice >> event_log
        event_log >> external_services
        external_services >> integration_db
        external_services >> payment_db_crm
        http_load_balancer >> mobile_app

    user >> dns >> load_balancer
    load_balancer >> Edge(color="brown") >> [
        accounts_summary, leads_summary, tasks_summary,
        permissions, orders, stats_internal,
        stats_external, ml_service, payment
    ]
    load_balancer >> Edge(color="blue") >> [
        crm_accounts_summary, crm_leads_summary, crm_tasks_summary,
        integration, crm_permissions, crm_orders,
        crm_stats_internal, crm_stats_external, crm_ml_service,
        crm_payment, fortification, mobile_app,
        api_gateway, auth_microservice, event_log,
        external_services, http_load_balancer
    ]
