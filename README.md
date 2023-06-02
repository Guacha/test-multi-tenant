# Multi-Tenant Django App with Multiple Schemas

This is a Django application that demonstrates multi-tenant architecture using multiple schemas for each tenant. The app is containerized using Docker and can be easily run using Docker Compose.

## Prerequisites

Before running the application, make sure you have the following installed:

- Docker
- Docker Compose

## Installation

1. Clone the repository:

```shell
git clone <repository-url>
```

2. Navigate to the project directory:

```shell
cd test-multi-tenant
```

3. Build the Docker image:

```shell
docker-compose build
```

4. Run the Docker containers:

```shell
docker-compose up
```

This will start the Django app along with the required PostgreSQL database containers for multi-tenant schemas.

## Usage

Once the Docker containers are up and running, you can access the Django app in your web browser at `http://localhost:8000`.

## Docs
https://django-tenant-schemas.readthedocs.io/en/latest/use.html
