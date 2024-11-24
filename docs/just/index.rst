Project Automation with justfile
---------------------------------

The ``justfile`` is a configuration file used to define and organize project tasks and commands. Below is a structured explanation of the commands defined in your `justfile` and how to use them effectively.

File Structure Overview
____________________________
This file automates common tasks for managing:
- Django development
- Servers (Gunicorn, uwsgi)
- Dependency management
- Database and cache resets
- Docker environments
- Task scheduling (Celery)

Using Just Commands
____________________________
To execute any command in the ``justfile``, run:

.. code-block:: bash

    just <command-name>

Available Commands
____________________________

Project Build and Development
=================================
- ``build``: Runs migrations and creates a superuser without errors for production.
- ``build-dev``: Prepares the development environment by creating a superuser without errors.

Server Management
=================================
- **Gunicorn**:
  - ``start-gunicorn``: Starts the Gunicorn server with production settings.
  - ``stop-gunicorn``: Stops the Gunicorn server.
  - ``restart-gunicorn``: Restarts the Gunicorn server.

- **uwsgi**:
  - ``start-uwsgi``: Starts the uwsgi server with production settings.
  - ``stop-uwsgi``: Stops the uwsgi server.
  - ``restart-uwsgi``: Restarts the uwsgi server.

Dependency Management
=================================
- ``install``: Installs required packages from ``requirements.txt`` using ``pip`` and ``uv``.

Django Development Server
=================================
- ``manage-start``: Starts the Django development server.
- ``manage-start-logfile``: Starts the server and logs output to ``logs/manage.log``.
- ``manage-stop-logfile``: Stops the development server running on port ``8080``.
- ``manage-restart-logfile``: Restarts the development server with logging enabled.

Log Management
=================================
- ``open-devlog``: Opens the development log file in real time using ``tail``.

Shell Access
=================================
- ``shell``: Opens the Django shell.

Cleaning Environment (Development Only)
=================================
- ``clean-project``: Cleans database, cache, and migration files.
- ``clean-migrations-cache``: Removes migration files except ``__init__.py``.
- ``rest-db``: Resets the database schema.
- ``rest-cache``: Clears the cache with confirmation prompt.

Database Operations
=================================
- ``migrate``: Creates and applies migrations.
- ``check_database``: Checks database connectivity without starting Django.

User Management
=================================
- ``create-admin``: Creates a Django superuser.
- ``create-admin-no-error``: Creates a superuser without error prompts.

Static Files Management
=================================
- ``collectstatic``: Collects all static files for deployment.

Translation Support
=================================
- ``makemessages``: Generates message files for all translatable strings.
- ``compilemessages``: Compiles translation files.

Testing
=================================
- ``cicd-test``: Runs the test suite using `pytest`.

Task Scheduling
=================================
- **Celery**:
  - ``celery-worker``: Starts the Celery worker.
  - ``celery-flower``: Starts the Celery Flower monitoring tool.
  - ``celery-beat``: Starts the Celery Beat scheduler.

Docker Management
=================================
- ``uv-docker``: Installs a package inside a Docker container.
- ``dev-docker``: Manages the development Docker environment.
- ``docs-docker``: Manages the Docker environment for documentation.
- ``uwsgi-docker``: Manages the production Docker environment with uwsgi.
- ``gunicorn-docker``: Manages the production Docker environment with Gunicorn.
- ``node-docker``: Manages the Docker environment for Node.js.

How to Use Hooks
____________________________
You can chain multiple tasks together using hooks. For example:

- **Build Command**: 
.. code-block:: bash

     just build

This runs both the ``migrate`` and ``create-admin-no-error`` commands sequentially.

- **Restart Gunicorn**:
.. code-block:: bash

     just restart-gunicorn

This stops and then starts the Gunicorn server.

Best Practices
____________________________

- **Development Only Commands**: Avoid running commands like ``rest-db`` or ``clean-project`` in production.
- **Environment Variables**: Ensure all necessary environment variables are set before starting servers.
- **Logs**: Monitor server logs using the ``open-devlog`` command for debugging.
- **Docker**: Use Docker-specific commands for isolated environments.

By automating repetitive tasks with ``justfile``, you can streamline project workflows and focus on development.
