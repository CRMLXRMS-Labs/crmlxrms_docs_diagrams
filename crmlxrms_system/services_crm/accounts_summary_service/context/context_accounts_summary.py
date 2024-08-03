from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

with Diagram("Accounts Summary Service - Context Diagram", direction="TB"):
    user = Person("CRM User", "Interacts with the CRM system")
    
    crm_system = System("CRM System", "Handles customer relationships")
    
    accounts_summary_service = Container(
        "Accounts Summary Service",
        ".NET Core",
        "Provides users with a summary of their accounts"
    )
    
    user >> Relationship("Requests account summary") >> crm_system
    crm_system >> Relationship("Delegates to") >> accounts_summary_service
