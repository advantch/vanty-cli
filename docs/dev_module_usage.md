## Vanty CLI - Development Module Usage

The `vanty` CLI tool provides a set of commands under the `dev` module to assist developers in managing their development environment and tasks. Below is a guide on how to use the `vanty dev` commands.

### Initializing the Project

To build the docker stack and initialize the project, use:

```bash
vanty dev init
```

This command will build the necessary Docker containers and prepare your development environment.

### Starting the Project

To start the project, run:

```bash
vanty dev start
```

This will start the docker stack along with any additional services such as Vite for frontend development.

### Running Migrations

To apply database migrations, execute:

```bash
vanty dev migrate
```

You can also pass additional options to the `migrate` command if needed.

### Creating a Superuser

To create a Django superuser, use:

```bash
vanty dev create-superuser
```

Follow the prompts to set up a new superuser for your application.

### Running Tests

To run tests for a specific Django app or file, use:

```bash
vanty dev run-tests <app_name> <file_name>
```

Replace `<app_name>` and `<file_name>` with the appropriate values for your project.

### Additional Commands

The `dev` module also includes commands for tasks such as rebuilding a specific Docker container, connecting to Stripe CLI, and copying static files. Use `vanty dev --help` to see all available commands and their usage.
