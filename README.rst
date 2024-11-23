Introduction
-------------
**octo-launch simplifies the setup process of Django projects for faster development.**

Why Octo-Launch?
=================

Octo-Launch works like an octopus, ready to start anywhere without any complexity.  
This framework is built to provide the best workflow to get started quickly, with only a few adjustments needed at the beginning of your project.  
It is an excellent choice for many projects that you may work on.

Can this template always be used in every project?
====================================================

The truth is no. This template cannot be used for every project.  
It will only be suitable if the project requires **Redis** and **Celery**,  
and if the project is built as an **API application**.  
In such cases, this template will be a great choice, offering you a very fast start and helping you get the most out of **Django**.

Will our team work on templates covering other scenarios?
==========================================================

There are indeed other templates that haven't been released yet.  
We might consider working on them in the future.

Getting Started
===============

Octo-Launch is designed so that anyone can run your project—even a child!  
With just a single command, you can get everything up and running in development mode:

.. code-block:: bash

    just dev-docker up

Environment Configuration
=========================

- An `.env` file will be created by default and configured to work with `dev-docker`.  
  If you already have a `.env` file, it will not be overwritten.  
  To understand the required configurations, check the `.env.template` file.  
  For the default configuration of the `dev-docker` container, refer to the `.env.dev` file.

Admin User Creation
===================

- Whenever the system starts, the first user will be created as an administrator,  
  and their credentials will be stored in the `.envs/.admin` file.

- During the development stage, you can:
  - Set static admin account credentials in `.envs/.admin`, or  
  - Leave them empty to generate random credentials.

- In the production stage, a random password will **always** be generated for the admin account.  
  Please do not keep the `.envs/.admin` file or use a static password in production.  
  You are encouraged to follow your own security practices.

.. code-block:: env

    # .envs/.admin
    email='admin@email.com'
    password='your-password'

Dependency on Just
==================

This template heavily relies on **Just**, a modern command runner, to simplify and automate project workflows.  
To take full advantage of this template, you need to have **Just** installed on your system.  

Follow the installation instructions provided in the official **Just** repository:  
`Just GitHub Repository <https://github.com/casey/just>`_

Features
========

- **Pre-configured Settings:** Essential settings are already configured, allowing you to focus on developing features rather than setup.
- **Ready-to-Use Commands:** `just <https://github.com/casey/just>`_ commands are provided to streamline project setup and management.
- **Celery and Redis Integration:** `Celery <https://github.com/celery/django-celery>`_ and `Redis <https://github.com/jazzband/django-redis>`_ have been added to the project, providing a suitable development environment for asynchronous task processing and caching.
- **API Development Focus:** The template focuses on developing an API interface, streamlining the creation and management of API endpoints.
- **Mailpit Integration:** `Mailpit <https://mailpit.axllent.org/>`_ has been added for email testing, allowing you to test email functionality easily during development.
- **Storage Configuration:** Pre-configured settings for both local and `S3 <https://aws.amazon.com/ar/pm/serv-s3/>`_ storage options are available, making it easy to switch between different storage backends.
- **Documentation with DRF-Spectacular:** Documentation is built using `DRF-Spectacular <https://drf-spectacular.readthedocs.io/en/latest/>`_, providing a comprehensive and user-friendly way to document your API.
- **Initial Applications:** Two applications, `users` and `accounts`, are pre-configured as starting points. These include basic operations for user creation and management, which can be customized further.
- **Sphinx Documentation Environment:** A `Sphinx <https://www.sphinx-doc.org/>`_ documentation environment is set up and ready to use, making it easy to generate and maintain project documentation.
- **App.json File:** An `config.app.json` file is included to supply application data once and manage it within the project, streamlining application configuration.
- **Docker Environments:** Both development and production environments are configured using `Docker <https://www.docker.com>`_, ensuring consistency across different stages of deployment.
- **Pytest Testing Environment:** A complete `pytest <https://pytest-django.readthedocs.io/en/latest/>`_ testing environment is set up, with pre-configured test files for `users` and `accounts` applications, facilitating thorough testing.
- **Use of `apps` Directory:** The project uses an `apps` directory to organize application files separately. This approach allows you to create new applications in each project without the need to rename the `apps` directory each time.
- **Manager Decorator:** A `manager` decorator is created to add custom commands to the `manage.py` file. Refer to the documentation for guidance on when and how to use this decorator.
- **UWSGI and Gunicorn:** Both `UWSGI <https://uwsgi-docs.readthedocs.io/>`_ and `Gunicorn <https://docs.gunicorn.org/>`_ are provided with basic production settings. It is recommended to fine-tune these settings to match your specific requirements.

These features make it easier to kickstart your development process, allowing you to concentrate on building your application's functionality.

Additional Features
===================

- **Ruff and Pre-commit Integration:**  
  This template utilizes `Ruff <https://github.com/charliermarsh/ruff>`_ as a fast and reliable linter, ensuring consistent code quality and adherence to Python standards.  
  Additionally, `pre-commit <https://pre-commit.com/>`_ is used to automate linting and formatting checks before commits are pushed, preventing potential issues early in the development process.  

- **GitHub Actions for CI/CD:**  
  The project uses `GitHub Actions <https://github.com/features/actions>`_ to automate testing and maintain continuous integration. Tests are run for every push and pull request to ensure that changes do not introduce bugs or break existing functionality.  

- **CodeQL for Security Analysis:**  
  To enhance code security, `CodeQL <https://codeql.github.com/>`_ is integrated within the GitHub Actions workflow. This feature provides automated static analysis to detect vulnerabilities and improve code robustness.

These tools and workflows are implemented to ensure a high-quality, secure, and maintainable codebase while streamlining the development process.

Getting Started
===============

To begin your project, you first need to install the framework:  

.. code-block:: bash

   pip install octo-framework

Once installed, you can start a new project by running:  

.. code-block:: bash

   octo startproject "your_project_name"

The project structure is well-organized, with separate applications placed inside the `/app` directory.  
If you want to add a new application, ensure you are in the root of your project and run:  

.. code-block:: bash

   octo startapp "your_app_name"

This will create a new application following the same structure as the main project.  
`read more <https://octo-launch.readthedocs.io/>`_