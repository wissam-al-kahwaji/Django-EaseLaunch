Docker Compose Documentation Service
-----------------------------------

The `docker-compose.gunicorn.yml` file defines the configuration for the Documentation service, which runs a Django-based documentation application.

The service is responsible for building and running the documentation in a container. It provides a development environment for managing and viewing the documentation.

.. code-block:: yaml

   services:
     docs:
       image: django_app_docs
       container_name: django_app_docs
       build:
         context: .
         dockerfile: ./compose/docs/Dockerfile
       env_file:
         - ./.envs/.env
       volumes:
         - .:/app:z
       ports:
         - '9000:9000'
       command: /start-docs

Configuration Breakdown:
===========================

- ``image``: Specifies the Docker image used for the container, in this case, `django_app_docs`.
- ``container_name``: The name assigned to the container when it is running, in this case, `django_app_docs`.
- ``build.context``: Specifies the build context, which is the current directory (`.`).
- ``dockerfile``: The path to the Dockerfile used for building the image, which is located at `./compose/docs/Dockerfile`.
- ``env_file``: Specifies the environment file (`.env`) used for setting environment variables inside the container.
- ``volumes``: Mounts the project directory (`.`) to the `/app` directory inside the container, with the `:z` flag to ensure proper labeling for SELinux compatibility.
- ``ports``: Maps port `9000` on the host machine to port `9000` inside the container, allowing access to the documentation service via `http://localhost:9000`.
- ``command``: The command that runs when the container starts, which is `/start-docs`. This command initializes the documentation server inside the container.

How to Run the Documentation Service:
===========================

To start the documentation service, you can use either of the following commands:

1. **Using Docker Compose**:

.. code-block:: shell

   docker-compose -f docker-compose.docs.yml up -d

This command will build the image (if not already built), start the container, and run the documentation server.

2. **Using Just**:

If you have `just` installed, you can start the documentation service using the following command:

.. code-block:: shell

   just docs-docker up -d

This will also start the container and run the documentation server.

Once the service is running, you can access the documentation by navigating to:

.. code-block:: text

   http://localhost:9000
