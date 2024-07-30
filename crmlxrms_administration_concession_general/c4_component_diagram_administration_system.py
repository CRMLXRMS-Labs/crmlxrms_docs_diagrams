from diagrams import Diagram, Cluster
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage

with Diagram("C4 Component Diagram - Administration Concession System Services", show=False):

    with Cluster("Administration Concession System"):
        accounts_summary = Rack("Accounts Summary Service")
        leads_summary = Rack("Leads Summary Service")
        tasks_summary = Rack("Tasks Summary Service")
        permissions = Rack("Permissions Service")
        orders = Rack("Orders Service")
        stats_internal = Rack("Statistics Service (internal)")
        stats_external = Rack("Statistics Service (external)")
        ml_service = Rack("ML Service")
        payment = Rack("Payment Service")

        accounts_db = Storage("Account Summary Data")
        leads_db = Storage("Leads Summary Data")
        tasks_db = Storage("Tasks Summary Data")
        permissions_db = Storage("Permissions Data")
        orders_db = Storage("Orders Data")
        stats_internal_db = Storage("Internal Stats Data")
        stats_external_db = Storage("External Stats Data")
        ml_db = Storage("ML Data")
        payment_db = Storage("Payment Data")

    accounts_summary >> accounts_db
    leads_summary >> leads_db
    tasks_summary >> tasks_db
    permissions >> permissions_db
    orders >> orders_db
    stats_internal >> stats_internal_db
    stats_external >> stats_external_db
    ml_service >> ml_db
    payment >> payment_db
