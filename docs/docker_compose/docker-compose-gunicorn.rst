Gunicorn and Nginx Deployment
-----------------------------

The following `docker-compose.yml` file defines a production-ready environment for deploying a Django application using Gunicorn as the application server and Nginx as the reverse proxy. The setup also includes additional services such as Celery workers, Celery beat, and Flower for task monitoring.

.. code-block:: yaml

   networks:
     django_gunicorn_network:
       driver: bridge

   services:
     django: &django
       build:
         context: .
         dockerfile: ./compose/django/Dockerfile
       image: django_app
       container_name: django_gunicorn
       networks:
         django_gunicorn_network:
       volumes:
         - .:/app:z
       env_file:
         - ./.envs/.env
       command: just build start-gunicorn
       restart: always

     nginx:
       image: nginx:latest
       container_name: nginx_gunicorn
       environment:
         PUID: 1000
         PGID: 1000
         TZ: Africa/Cairo
       depends_on:
         - django
       networks:
         django_gunicorn_network:
       volumes:
         - ./compose/nginx/gunicorn:/etc/nginx/conf.d
         - .:/app:z
       ports:
         - 80:80
         - 443:443
       restart: always

     celeryworker:
       <<: *django
       image: celeryworker_django_app
       container_name: celeryworker_django_app
       ports: []
       command: just celery-worker
       restart: always

     celerybeat:
       <<: *django
       image: celerybeat_django_app
       container_name: celerybeat_django_app
       ports: []
       command: just celery-beat
       restart: always

     flower:
       <<: *django
       image: flower_django_app
       container_name: flower_django_app
       command: just celery-flower
       ports:
         - 5555:5555
       restart: always

Configuration Details
=================

1. **Networks**:
   - ``django_gunicorn_network``: Defines a bridge network for connecting services.

2. **Services**:
   - **Django**:
     - Runs the Django application with Gunicorn as the application server.
     - Built using the Dockerfile located at `./compose/django/Dockerfile`.
     - Environment variables are loaded from `./.envs/.env`.
     - The container automatically restarts on failure (`restart: always`).
     - Starts with the command `just build start-gunicorn`.
   - **Nginx**:
     - Acts as the reverse proxy for the Gunicorn application.
     - Uses configuration files from `./compose/nginx/gunicorn`.
     - Exposes HTTP on port `80` and HTTPS on port `443`.
     - Depends on the Django service to ensure it starts after the application is ready.
   - **Celery Worker**:
     - Handles background tasks.
     - Uses the `just celery-worker` command to start.
   - **Celery Beat**:
     - Schedules periodic tasks.
     - Uses the `just celery-beat` command to start.
   - **Flower**:
     - Provides a web-based UI for monitoring Celery tasks.
     - Accessible at port `5555`.

How to Start the Deployment
=================

1. **Using Docker Compose**:

.. code-block:: shell

   docker-compose -f docker-compose.yml up -d

2. **Using Just**:

.. code-block:: shell

   just dev-docker up -d

After starting, the application will be available on:

.. code-block:: text

   http://localhost:80

For Flower monitoring:

.. code-block:: text

   http://localhost:5555

.. note::

   **Disclaimer**: 
   This setup is **not intended for production use** as-is. These configurations are basic settings designed to help you get started quickly with your application. It is your responsibility to modify these settings to fit your specific application requirements and hosting environment. 

   We are **not responsible** for any issues or failures that occur in production environments. Ensure you:
   - Review and update environment variables.
   - Implement secure and scalable configurations.
   - Test thoroughly before deploying to production.

   Use this setup as a starting point, not a comprehensive production-ready solution.
