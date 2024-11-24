.. _octo_logging:

Logging with ``octo.logging``
============================

The ``octo.logging`` module provides a flexible and easy-to-use setup for handling logging in Django applications. It includes utilities to initialize loggers with structured configurations and manage log outputs.

Overview
--------

The logging system includes:
- ``Logger``: A class for quick and automated logger creation and configuration.
- ``get_logging``: A utility function to dynamically generate a logging configuration.
- Integration with Django settings to customize logger behavior via the ``OCTO_LOGGER_NAME`` setting.

How It Works
------------

When you initialize a logger using the ``Logger`` class, the system will:
1. Automatically create a log file in the ``/logs`` directory inside your Django ``BASE_DIR``.
2. Use the provided logger name to name the log file (e.g., ``custom_logger.log``).
3. Set up the logger for immediate use, ensuring that all logs are written to the corresponding file.

This provides a fast and efficient way to create and use loggers without manual configuration.

Usage Example
-------------

To set up a logger and use it in your project, follow these steps:

.. code-block:: python

    from octo.logging import Logger, sanitize_message

    # Initialize the logger
    logger = Logger(namefile="custom_logger").get()

    # Log a sanitized message
    raw_message = "This is a\nmultiline\tmessage."
    clean_message = sanitize_message(raw_message)
    logger.info(clean_message)

In this example:
- A log file named ``custom_logger.log`` will be created in the ``/logs`` directory.
- All log messages will be written to this file with a color-coded format in the console.

Logger Initialization
----------------------

The ``Logger`` class provides a straightforward way to create a logger:

.. code-block:: python

    from octo.logging import Logger

    # Create a logger with a custom name
    logger = Logger(namefile="app_logger").get()

    # Start logging messages
    logger.debug("This is a debug message")
    logger.error("This is an error message")

If the provided ``namefile`` is ``"app_logger"``, a log file named ``app_logger.log`` will be created in ``/logs``.

Features
--------

- **Automatic File Creation**: Any ``namefile`` provided will result in the creation of a ``.log`` file inside ``/logs``.
- **Immediate Logging**: The logger is ready to use as soon as it is initialized.
- **Customizable**: You can customize the logger format, level, and output file location by modifying the ``get_logging`` function.

Sanitizing Log Messages
-----------------------

Use ``sanitize_message`` to clean raw log messages by removing unwanted characters such as newlines or tabs.

.. code-block:: python

    from octo.logging import sanitize_message

    raw_message = "This is a\nmessy\tmessage."
    clean_message = sanitize_message(raw_message)
    print(clean_message)  # Output: "This is a messy message."

Adding Loggers in Settings
--------------------------

If no ``namefile`` is provided during the logger initialization in the ``Logger`` class, the default logger name will be determined by the ``OCTO_LOGGER_NAME`` setting in your Django settings file. If the ``OCTO_LOGGER_NAME`` setting is not defined, the default logger name will fall back to ``"octo-log"``.

You can define the default logger name in your settings file as follows:

.. code-block:: python

   OCTO_LOGGER_NAME = "my_custom_logger"

Example Usage Without Specifying ``namefile``
-------------------------------------------

When initializing the logger without providing a ``namefile``, the default logger name will be used:

.. code-block:: python

    from octo.logging import Logger

    # Initialize logger without specifying namefile
    logger = Logger().get()

    # Log a message
    logger.info("This log uses the default logger name!")

In this example:
- If ``OCTO_LOGGER_NAME = "my_custom_logger"`` is set in your Django settings, the log file will be named ``my_custom_logger.log`` and saved in the ``/logs`` directory.
- If ``OCTO_LOGGER_NAME`` is not set, the log file will default to ``octo-log.log``.

This approach allows you to quickly use logging without manually specifying the log file name in each instance.

This system simplifies logging, ensuring rapid setup and easy debugging with minimal effort.
