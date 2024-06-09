# octo-launch
**octo-launch simplifies the setup process of Django projects for faster development.**

### Features
**This template includes several pre-configured additions to help you save time and get started with development faster**
- **Pre-configured Settings:** Essential settings are already configured, allowing you to focus on developing features rather than setup.
- **Integrated Docker Support:** Docker configurations are included to simplify containerization and environment consistency.
- **Ready-to-Use Commands:** [just](https://github.com/casey/just) commands are provided to streamline project setup and management.
- **Celery and Redis Integration**: Celery and Redis have been added to the project, providing a suitable development environment for asynchronous task processing and caching.
- **API Development Focus**: The template focuses on developing an API interface, streamlining the creation and management of API endpoints.
- **Mailpit Integration**: Mailpit has been added for email testing, allowing you to test email functionality easily during development.
- **Storage Configuration**: Pre-configured settings for both local and S3 storage options are available, making it easy to switch between different storage backends.
- **Documentation with DRF-Spectacular**: Documentation is built using DRF-Spectacular, providing a comprehensive and user-friendly way to document your API.
- **Initial Applications**: Two applications, `users` and `accounts`, are pre-configured as starting points. These include basic operations for user creation and management, which can be customized further.
- **Sphinx Documentation Environment**: A Sphinx documentation environment is set up and ready to use, making it easy to generate and maintain project documentation.
- **App.json File**: An `app.json` file is included to supply application data once and manage it within the project, streamlining application configuration.
- **Docker Environments**: Both development and production environments are configured using Docker, ensuring consistency across different stages of deployment.
- **Pytest Testing Environment**: A complete pytest testing environment is set up, with pre-configured test files for `users` and `accounts` applications, facilitating thorough testing.
- **Use of `apps` Directory**: The project uses an `apps` directory to organize application files separately. This approach allows you to reuse the template across multiple projects without renaming files.
- **Manager Decorator**: A `manager` decorator is created to add custom commands to the `manage.py` file. Refer to the documentation for guidance on when and how to use this decorator.
- **UWSGI and Gunicorn**: Both UWSGI and Gunicorn are provided with basic production settings. It is recommended to fine-tune these settings to match your specific requirements.

These features make it easier to kickstart your development process, allowing you to concentrate on building your application's functionality.



### Get Started
- You can Just run dev-docker to start development mode
```bash
just dev-docker up
```
- An .env file will be created by default and configured to work with dev-docker. If you created a previous .env file, it will not be created by default. You can look at .env.template to understand the required configurations and .env.dev to know the default configuration of the dev-docker container.
- Whenever the system starts, the first user will be created as an administrator, and their data will be generated inside the .envs/.admin file. During the development stage, you can set the admin account data to be static, or you can leave it empty to be generated randomly. In the production stage, a random password will be generated mandatorily. Please do not keep the file or change the password during production, or follow your own security method.
```.env
# .envs/.admin
email='admin@email.com'
password='your-password'
```
