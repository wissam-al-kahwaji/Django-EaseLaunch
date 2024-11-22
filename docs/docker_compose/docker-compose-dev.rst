Development Environment Setup Using Docker Compose
--------------------------------------------------

The ``docker-compose.dev.yml`` file is used to set up a development environment using Docker Compose. It defines multiple services that work together within a single network. These services include the Django application, PostgreSQL database, Redis, Celery, Flower, and others.

Networks
==================
In this section, a custom network is defined to connect all containers. The ``bridge`` driver is used to link the containers together within a specific subnet.

.. code-block:: yaml

   networks:
     django_network:
       driver: bridge
       ipam:
         config:
           - subnet: 173.14.0.0/24

- ``django_network``: A custom bridge network that connects all containers.
- ``ipam``: Stands for IP Address Management, used here to define the subnet ``173.14.0.0/24``.

Volumes
==================
This section defines volumes to ensure data persists across container restarts. The volumes are used to store PostgreSQL and Redis data.

.. code-block:: yaml

   volumes:
       postgres_data:
       redis_data:

- ``postgres_data``: Volume used to persist PostgreSQL data.
- ``redis_data``: Volume used to persist Redis data.

Services
==================
Several services are defined in this file, each running within its own container and interconnected via the ``django_network`` network.

Django Service
______________________
The Django service runs the main application, built from the provided Dockerfile, and configured with necessary environment variables and dependencies.

.. code-block:: yaml

   django:
       build:
         context: .
         dockerfile: ./compose/django/Dockerfile
       image: django_app
       container_name: django_dev
       networks:
         django_network:
       depends_on:
         - redis
         - postgres
       volumes:
         - .:/app:z
       env_file:
         - ./.envs/.env
       ports:
         - 8080:8080
       command: just build-dev manage-start-logfile open-devlog

- ``build.context``: Specifies the build context (current directory).
- ``dockerfile``: Path to the Dockerfile used for building the Django image.
- ``image``: The name of the image used for the Django container.
- ``container_name``: The name of the container for the Django service.
- ``networks``: The network the container connects to (``django_network``).
- ``depends_on``: Specifies the services that must be started before Django (Redis and PostgreSQL).
- ``volumes``: Mounts the current directory to the ``/app`` directory in the container.
- ``env_file``: Specifies the environment file used to set environment variables for the container.
- ``ports``: Maps port ``8080`` on the host to port ``8080`` on the container.
- ``command``: Defines the command to run the Django application.

PostgreSQL Service
______________________
The PostgreSQL service runs the database used by the Django application.

.. code-block:: yaml

   postgres:
       image: postgres:latest
       container_name: postgres_dev
       environment:
         POSTGRES_USER: postgres
         POSTGRES_PASSWORD: postgres
         POSTGRES_DB: django_db
       networks:
         django_network:
       volumes:
         - postgres_data:/var/lib/postgresql/data
       ports:
         - 5432:5432

- ``image``: The Docker image used for PostgreSQL (``postgres:latest``).
- ``container_name``: The name of the PostgreSQL container.
- ``environment``: Environment variables used to configure the PostgreSQL database.
- ``networks``: The network the container connects to (``django_network``).
- ``volumes``: Mounts the ``postgres_data`` volume to persist PostgreSQL data.
- ``ports``: Maps port ``5432`` on the host to port ``5432`` on the container.

Mailpit Service
______________________
The Mailpit service provides a local mail server for development and testing.

.. code-block:: yaml

   mailpit:
       image: docker.io/axllent/mailpit:latest
       container_name: mailpit_dev
       networks:
         django_network:
       ports:
         - 8025:8025
         - 1025:1025

- ``image``: The Docker image used for Mailpit (``docker.io/axllent/mailpit:latest``).
- ``container_name``: The name of the Mailpit container.
- ``networks``: The network the container connects to (``django_network``).
- ``ports``: Maps port ``8025`` and ``1025`` on the host to ports on the container.

Redis Service
______________________
The Redis service provides a caching layer for the Django application.

.. code-block:: yaml

   redis:
       image: redis:latest
       container_name: redis_dev
       networks:
         django_network:
       volumes:
         - redis_data:/data
       ports:
         - 6379:6379

- ``image``: The Docker image used for Redis (``redis:latest``).
- ``container_name``: The name of the Redis container.
- ``networks``: The network the container connects to (``django_network``).
- ``volumes``: Mounts the ``redis_data`` volume to persist Redis data.
- ``ports``: Maps port ``6379`` on the host to port ``6379`` on the container.

RedisInsight Service
______________________
The RedisInsight service provides a web interface to monitor Redis.

.. code-block:: yaml

   redisinsight:
       image: redis/redisinsight:latest
       container_name: redisinsight_dev
       networks:
         django_network:
       depends_on:
         - redis
       ports:
         - 5540:5540

- ``image``: The Docker image used for RedisInsight (``redis/redisinsight:latest``).
- ``container_name``: The name of the RedisInsight container.
- ``networks``: The network the container connects to (``django_network``).
- ``depends_on``: Specifies the service that must be started before RedisInsight (Redis).
- ``ports``: Maps port ``5540`` on the host to port ``5540`` on the container.

Celery Worker Service
______________________
The Celery worker service runs background tasks for the Django application.

.. code-block:: yaml

   celeryworker:
       <<: *django
       image: celeryworker_dev
       container_name: celeryworker_dev
       depends_on:
         - redis
         - postgres
         - mailpit
         - django
       ports: []
       command: just celery-worker

- ``<<: *django``: Inherits configuration from the Django service.
- ``image``: The name of the Celery worker image.
- ``container_name``: The name of the Celery worker container.
- ``depends_on``: Specifies the services that must be started before Celery (Redis, PostgreSQL, Mailpit, Django).
- ``command``: Defines the command to start the Celery worker.

Celery Beat Service
______________________
The Celery Beat service runs scheduled tasks for the Django application.

.. code-block:: yaml

   celerybeat:
       <<: *django
       image: celerybeat_dev
       container_name: celerybeat_dev
       depends_on:
         - redis
         - postgres
         - mailpit
         - django
       ports: []
       command: just celery-beat

- ``<<: *django``: Inherits configuration from the Django service.
- ``image``: The name of the Celery Beat image.
- ``container_name``: The name of the Celery Beat container.
- ``depends_on``: Specifies the services that must be started before Celery Beat (Redis, PostgreSQL, Mailpit, Django).
- ``command``: Defines the command to start Celery Beat.

Flower Service
______________________
The Flower service provides a web interface to monitor Celery tasks.

.. code-block:: yaml

   flower:
       <<: *django
       image: flower_dev
       container_name: flower_dev
       depends_on:
         - redis
         - postgres
         - mailpit
         - django
       ports:
         - 5555:5555
       command: just celery-flower

- ``<<: *django``: Inherits configuration from the Django service.
- ``image``: The name of the Flower image.
- ``container_name``: The name of the Flower container.
- ``depends_on``: Specifies the services that must be started before Flower (Redis, PostgreSQL, Mailpit, Django).
- ``ports``: Maps port ``5555`` on the host to port ``5555`` on the container.
- ``command``: Defines the command to run Flower.

Node Service
______________________
The Node service runs the frontend application. In this setup, Next.js is used, but you can replace it with any other frontend framework or remove this configuration if it's not needed.

.. code-block:: yaml

   node:
       build:
         context: .
         dockerfile: ./compose/node/Dockerfile
       image: frontend_app
       container_name: frontend_dev
       networks:
         django_network:
       volumes:
         - ./frontend:/app
         - /app/node_modules
       ports:
         - "3000:3000"
       command: npm run dev

- ``build.context``: Specifies the build context (current directory).
- ``dockerfile``: Path to the Dockerfile used for building the Node image.
- ``image``: The name of the image used for the Node container.
- ``container_name``: The name of the Node container.
- ``networks``: The network the container connects to (``django_network``).
- ``volumes``: Mounts the frontend directory and node_modules to the container.
- ``ports``: Maps port ``3000`` on the host to port ``3000`` on the container.
- ``command``: Defines the command to start the frontend application (using Next.js in this case).

Conclusion
==================
This ``docker-compose.dev.yml`` file provides an integrated development environment with all the services needed for developing and testing the Django application, including databases, caching, background task processing, email testing, and the frontend.

How to Run the Container
==================

A Docker container has been carefully built to be robust during development. You can develop the Django project inside this container and use the `devcontainer` feature. The container has been built to ensure that it does not stop in case of any issues, meaning it will continue running even if errors occur. This allows you to rely on the container entirely without interruption, avoiding the need to use your system's environment for error handling.

Note that the project heavily depends on `just`, so you will find `just` available inside the development environment. We have provided everything you need to get started and focus on your project idea.

You can run the container if you have `just` installed on your system using the following command:

.. code-block:: shell

   just dev-docker up -d

If you don't have `just` and only have Docker installed, you can run the container using the traditional method:

.. code-block:: shell

   docker compose -f docker-compose.dev.yml up -d
