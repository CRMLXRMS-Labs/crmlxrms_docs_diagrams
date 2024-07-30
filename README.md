Here is a sample README file for your repository:

```markdown
# CRM/LXRMS Documentation and Diagrams

This repository contains the documentation and diagrams for the CRM/LXRMS system. It provides a detailed overview of the system architecture, including the services, databases, and event flows.

## Directory Structure

```
.
├── administration_concession_system
├── crmlxrms_administration_concession_general
├── crmlxrms_system
├── .git
└── requirements.txt
```

- **administration_concession_system**: Contains documentation and diagrams related to the administration concession system.
- **crmlxrms_administration_concession_general**: Contains general documentation and diagrams for the CRM/LXRMS administration concession.
- **crmlxrms_system**: Contains the main CRM/LXRMS system documentation and diagrams.
- **.git**: Git repository files.
- **requirements.txt**: List of dependencies required for generating the diagrams.

## CRM/LXRMS System Overview

The CRM/LXRMS system is designed to manage customer relationships and logistics. It consists of several microservices, each responsible for different aspects of the system. The system uses a RabbitMQ event bus for handling events between services and Fabio Load Balancer for load balancing HTTP requests.

### Components of CRM in Basic internal version

1. **API Gateway Interface**: Entry point for API requests.
2. **Fabio Load Balancer**: Balances the load among HTTP clients using Consul.
3. **Event Bus**: Handles events within the system using RabbitMQ.
4. **Microservices**:
   - Accounts Summary Service
   - Leads Summary Service
   - Tasks Summary Service
   - Integration Service
   - Permissions Service
   - Orders Service
   - Internal Statistics Service
   - External Statistics Service
   - ML Service
   - Payment Service
   - Fortification System Service
   - Authorization Microservice
   - Operation External Services
5. **Databases**: Each service has its own MongoDB database for storing data.

### Event Flow (CRM Internam Event circulation)

Each service can send and consume events via the RabbitMQ event bus. The following events are examples of events sent and consumed by the services:

- **Accounts Summary Service**:
  - Sends: `AccountCreatedEvent`, `AccountUpdatedEvent`
  - Consumes: `AccountCreatedEvent`, `AccountUpdatedEvent`
- **Leads Summary Service**:
  - Sends: `LeadCreatedEvent`, `LeadUpdatedEvent`
  - Consumes: `LeadCreatedEvent`, `LeadUpdatedEvent`
- **Tasks Summary Service**:
  - Sends: `TaskCreatedEvent`, `TaskUpdatedEvent`
  - Consumes: `TaskCreatedEvent`, `TaskUpdatedEvent`
- **Integration Service**:
  - Sends: `IntegrationDataUpdatedEvent`
  - Consumes: `IntegrationDataUpdatedEvent`
- **Permissions Service**:
  - Sends: `PermissionGrantedEvent`, `PermissionRevokedEvent`
  - Consumes: `PermissionGrantedEvent`, `PermissionRevokedEvent`
- **Orders Service**:
  - Sends: `OrderPlacedEvent`, `OrderCancelledEvent`
  - Consumes: `OrderPlacedEvent`, `OrderCancelledEvent`
- **Internal Statistics Service**:
  - Sends: `InternalMetricsUpdatedEvent`
  - Consumes: `InternalMetricsUpdatedEvent`
- **External Statistics Service**:
  - Sends: `ExternalMetricsUpdatedEvent`
  - Consumes: `ExternalMetricsUpdatedEvent`
- **ML Service**:
  - Sends: `PredictionResultEvent`
  - Consumes: `PredictionResultEvent`
- **Payment Service**:
  - Sends: `PaymentProcessedEvent`, `PaymentFailedEvent`
  - Consumes: `PaymentProcessedEvent`, `PaymentFailedEvent`
- **Fortification System Service**:
  - Sends: `SecurityAlertEvent`, `SecurityUpdateEvent`
  - Consumes: `SecurityAlertEvent`, `SecurityUpdateEvent`
- **Authorization Microservice**:
  - Sends: `UserAuthenticatedEvent`, `UserAuthorizationUpdatedEvent`
  - Consumes: `UserAuthenticatedEvent`, `UserAuthorizationUpdatedEvent`

## Installation

To generate the diagrams, you need to install the dependencies listed in `requirements.txt`. Use the following command to install them:

```bash
pip install -r requirements.txt
```