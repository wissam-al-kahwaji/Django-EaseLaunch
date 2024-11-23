uWSGI Deployment Setup
----------------------

This configuration defines a **Docker Compose setup** to run a Django application with uWSGI, NGINX, and supporting services such as Celery and Flower. This setup is a starting point for deploying Django applications in a containerized environment with uWSGI.

Network Configuration
=======================
The `django_uwsgi_network` network is used to connect the containers in this setup.

.. code-block:: yaml

   networks:
     django_uwsgi_network:
       driver: bridge

Services
=======================
1. **Django Service**
   Runs the Django application using uWSGI.

   .. code-block:: yaml

      django:
        build:
          context: .
          dockerfile: ./compose/django/Dockerfile
        image: django_app
        container_name: django_uwsgi
        networks:
          django_uwsgi_network:
        volumes:
          - .:/app:z
        env_file:
          - ./.envs/.env
        ports:
          - 8080:8080
        command: just build start-uwsgi
        restart: always

   - **build.context**: Specifies the build context (current directory).
   - **dockerfile**: Path to the Dockerfile for building the Django image.
   - **image**: Name of the image used for the Django service.
   - **container_name**: Name of the Django container.
   - **networks**: Attaches the container to `django_uwsgi_network`.
   - **volumes**: Mounts the project directory to the container.
   - **ports**: Maps port `8080` on the host to port `8080` on the container.
   - **command**: Executes the `just build` command followed by `start-uwsgi` to launch the application.
   - **restart**: Ensures the container restarts automatically if it fails.

2. **NGINX Service**
   Serves as a reverse proxy to the Django application.

   .. code-block:: yaml

      nginx:
        image: nginx:latest
        container_name: nginx_uwsgi
        environment:
          PUID: 1000
          PGID: 1000
          TZ: Africa/Cairo
        depends_on:
          - django
        networks:
          django_uwsgi_network
        volumes:
          - ./compose/nginx/uwsgi:/etc/nginx/conf.d
          - .:/app:z
        ports:
          - 80:80
          - 443:443
        restart: always

   - **image**: Uses the latest NGINX image.
   - **container_name**: Names the NGINX container.
   - **environment**: Sets the user ID, group ID, and timezone.
   - **depends_on**: Ensures NGINX starts after the Django service.
   - **volumes**: Mounts NGINX configuration files and the project directory.
   - **ports**: Exposes ports `80` and `443` for HTTP and HTTPS.
   - **restart**: Automatically restarts the container upon failure.

3. **Celery Worker Service**
   Processes background tasks for the Django application.

   .. code-block:: yaml

      celeryworker:
        <<: *django
        image: celeryworker_django_app
        container_name: celeryworker_django_app
        ports: []
        command: just celery-worker
        restart: always

   - Extends the Django configuration.
   - Runs the `celery-worker` command to process tasks.

4. **Celery Beat Service**
   Handles periodic tasks scheduling.

   .. code-block:: yaml

      celerybeat:
        <<: *django
        image: celerybeat_django_app
        container_name: celerybeat_django_app
        ports: []
        command: just celery-beat
        restart: always

   - Extends the Django configuration.
   - Runs the `celery-beat` command to manage periodic tasks.

5. **Flower Service**
   Provides a web interface for monitoring Celery tasks.

   .. code-block:: yaml

      flower:
        <<: *django
        image: flower_django_app
        container_name: flower_django_app
        ports:
          - 5555:5555
        command: just celery-flower
        restart: always

   - Extends the Django configuration.
   - Exposes port `5555` for Flower's web interface.

.. note::

   **Disclaimer**: 
   This setup is **not intended for production use** as-is. These configurations are basic settings designed to help you get started quickly with your application. It is your responsibility to modify these settings to fit your specific application requirements and hosting environment. 

   We are **not responsible** for any issues or failures that occur in production environments. Ensure you:
   - Review and update environment variables.
   - Implement secure and scalable configurations.
   - Test thoroughly before deploying to production.

   Use this setup as a starting point, not a comprehensive production-ready solution.
