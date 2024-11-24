Project Structure and Creating New Applications
-----------------------------------------------

Current Project Structure
=========================

The project is organized into modular Django applications, following a clean and maintainable structure. Below is an example of the current structure:

.. code-block:: text

    app/
    ├── __pycache__/
    ├── account/
    │   ├── migrations/
    │   ├── serializers/
    │   ├── tests/
    │   ├── views/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── urls.py
    │   └── ...
    │
    └── urls.py  # Main routing file

The **`app/account`** directory, for instance, contains modules like `models.py`, `views/`, and `urls.py`, which collectively handle account-related features.

**`user`** and **`account`** Applications
=========================================

The project includes two essential applications, **`user`** and **`account`**, which are already documented in the API documentation.  
These applications provide core functionalities and can be customized or extended to meet the specific requirements of your project.  

For more details on how to interact with these applications programmatically, please refer to the API documentation.

Creating New Applications
=========================

To maintain modularity and consistency in the project, developers are required to use the **`octo`** CLI command to create new applications. This ensures that the new application is initialized with the appropriate structure.

Command Syntax
==============

.. code-block:: bash

    octo startapp "your_app_name"

Example Usage
=============

If you want to create a new application called **`blog`**, run the following command:

.. code-block:: bash

    octo startapp blog

This will create a directory structure similar to the one for the `account` app, with all necessary files initialized for development.

Integrating New Applications
============================

1. After creating the new application, include it in the **`INSTALLED_APPS`** section of your project's `settings.py` file.
   
2. Add the application's `urls.py` to the main URL routing file (`app/urls.py`) to ensure its routes are accessible.

For example:

.. code-block:: python

    from django.urls import include, path

    urlpatterns = [
        path('account/', include('app.account.urls')),
        path('user/', include('app.user.urls')),  # Include the user app
        path('blog/', include('app.blog.urls')),  # Add the new app here
    ]

Future Development
==================

This approach makes it easy to scale the project by adding new features as separate applications, ensuring better separation of concerns and reusability.
