Project Configuration Structure
-------------------

The project's configuration has been designed to be modular, flexible, and organized to handle different environments effectively. Below is a detailed explanation of the configuration files and their purposes.

Configuration Files
_____________________

Base Configuration
==================
**Path**: ``config/settings/base.py``

- This file contains the **core settings** that are shared across all environments.

Development Configuration
==================
**Path**: ``config/settings/development.py``

- Contains settings specific to the **development environment**.

Production Configuration
==================
**Path**: ``config/settings/production.py``

- Contains settings specific to the **production environment**.
Testing Configuration
==================
**Path**: ``config/settings/test.py``

- Contains settings specific to the **testing environment**.

Additional Configuration Files
________________________________

Application Metadata
==================
**Path**: ``config/app.py``

- An optional but useful file to store metadata or configuration for the application itself.

Storage Utilities
==================
**Path**: ``config/utils/storages.py``

- Designed to handle storage-related utilities and preferences.
- Pre-configured with AWS S3 storage integration, as this is the default storage mechanism used for `caodlly.com`.
- Developers can add or modify storage configurations as per project requirements.

Custom Command Manager
______________

The **Custom Command Manager** is designed to simplify the creation, execution, and management of project-specific commands. Unlike Django's default `manage.py` commands, it offers more flexibility and independence, making it ideal for lightweight execution or tasks outside the standard Django workflow.

Features
==================
- **Customizable**: Allows you to create commands tailored to your project requirements.
- **Independent Execution**: Commands can run without the full Django runtime.
- **Enhanced Workflow**: Useful for deployment pipelines, database checks, and more.

Overview of the Manager
==================

The `Manager` class is the core of this system. It handles command registration and execution. Each command is added to the manager schema, making it easily accessible via command-line arguments.

**Key Methods in Manager**:
- ``set_schema``: Registers commands by associating unique keys with command classes.
- ``setup``: Initializes the command execution process.

**Example of Manager Setup**:

.. code-block:: python

    from octo.handler.manager import Manager
    from .command import CreateSuperUser, DBConnect

    _manager = Manager()
    _manager.set_schema(
        {
            "createsuperuser": CreateSuperUser,
            "check_database": DBConnect,
        }
    )

    def manager(func):
        """Decorator to handle custom command execution."""
        def wrapper():
            try:
                return _manager.setup()
            except Exception as e:
                print(e)
                exit(1)
        return wrapper

Creating and Adding a Command
==================
1. **Create a Command Class**  
   Create a new class inheriting from `Command`. Implement the `handle` method to define the command logic.  

   Example:  

   .. code-block:: python

      from octo.handler.command import Command

      class DBConnect(Command):
          """Verify database connection"""

          def handle(self):
              from django.db import connections
              from django.db.utils import OperationalError

              try:
                  connections["default"].cursor().execute("SELECT 1")
                  print("Database connection successful.")
              except OperationalError as e:
                  print(f"Database connection failed: {e}")

2. **Register the Command with the Manager**  
   Add your command to the `Manager` schema:

   .. code-block:: python

      from .command import DBConnect
      _manager.set_schema(
          {
              "check_database": DBConnect,
          }
      )

3. **Execute the Command**  
   Use the command name registered in the schema to execute it from the command line:

   .. code-block:: bash

      python manage.py check_database

Using the `Command` Base Class
==================

The `Command` class provides the following features:

- **Hooks**: Add custom arguments (e.g., `--no-error`) using the `set_hooks` method.
- **Error Handling**: Enable or disable error messages with the `debug` attribute.
- **Django Environment**: Automatically initializes the Django environment when needed.

**Example of a Command with Hooks**:

.. code-block:: python

   class MyCustomCommand(Command):
       """A sample command with hooks"""

       def no_error(self):
           """Disable error messages."""
           self.debug = False

       def handle(self):
           print("Custom command logic executed.")

       def setup(self):
           self.set_hooks({"--no-error": "no_error"})
           super().setup()

4. **Run a Command with a Hook**  
   Hooks are additional flags you can pass alongside the command. For example:

   .. code-block:: bash

      python manage.py <command-name> --no-error

   In this case, the hook `--no-error` will disable error messages by calling the `no_error` method in the command class.

Detailed Command Execution Workflow
==================

1. **Define Command Logic**: Place the logic in the `handle` method.
2. **Set Custom Hooks**: Use `set_hooks` to add additional arguments if needed.
3. **Test Command Locally**: Run the command using `python manage.py <command-name>`.

Advantages of Using Manager
==================

- **Scalability**: Easily add multiple commands without cluttering your project structure.
- **Reusability**: Commands can be reused across different projects or environments.
- **Improved Organization**: Keeps custom commands separated from Django’s default commands.

Example Commands in Action
==================

1. **Verify Database Connection**:

   .. code-block:: bash

      python manage.py check_database

   **Output**:  

   - *Success*: "Database connection successful."
   - *Failure*: "Database connection failed: <error-message>"

2. **Create Superuser** (Example Command):

   .. code-block:: bash

      python manage.py createsuperuser

   This command uses the custom logic defined in the `CreateSuperUser` class.

3. **Run with Hooks**:

   .. code-block:: bash

      python manage.py check_database --no-error

   **Explanation**:  
   - The `--no-error` hook disables error messages, as defined in the `no_error` method of the `Command` class.

---

With the `Manager` and `Command` setup, you can easily extend the functionality of your project and integrate custom workflows tailored to your needs.


Usage Tips
 ==================

- **Environment Selection**:
  - Choose the appropriate settings file (``development``, ``production``, or ``test``) based on your environment.
  - Use environment variables or command-line flags to specify the settings file dynamically.

- **Customization**:
  - Extend the ``storages.py`` file to add new storage backends if required.
  - Add new commands to the `manager` for project-specific tasks.

- **Best Practices**:
  - Always use ``base.py`` for common settings to reduce redundancy.
  - Keep sensitive production settings (e.g., API keys) in environment variables and reference them in ``production.py``.

By following this structure, developers can easily adapt the project to different environments while maintaining clean and organized configuration files.

