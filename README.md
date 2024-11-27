# Order placement and management for zipline

Zipline both flies autonomous vehicles and operates a full-fledged logistics system. We run
operations out of our distribution centers, which we call "nests.
" At a given nest, we have an
inventory of medical supplies and a team of operators who manage that inventory and process
orders from doctors.
This repository contains the backend services and APIs for managing orders and inventory at Zipline nests. The system allows operators to:

- Track inventory levels of medical supplies
- Process incoming orders from healthcare facilities
- Manage product information (weights, descriptions, etc.)
- Monitor order status and delivery progress

## System Architecture

The system consists of several microservices:

- **Inventory Service**: Manages product catalog and inventory levels
- **Order Service**: Handles order placement and processing
- **Delivery Service**: Coordinates with flight systems for deliveries

## Prerequisites

- Python 3.8+
- PostgreSQL
- Docker & Docker Compose

## Local Development Setup

1. Clone the repository:

## Steps

- docker-compose # must have Docker prerequisite.

- source ./venv/bin/activate

- pip install -r requirements.txt


