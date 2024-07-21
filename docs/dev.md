

## Development Module Usage

The `vanty dev` module provides commands for managing your development environment and tasks.

### Initializing the Project

To build the docker stack and initialize the project:

```bash
vanty dev init
```

This command builds necessary Docker containers and prepares your development environment.

### Starting the Project

To start the project:

```bash
vanty dev start
```

This starts the docker stack along with additional services like Vite for frontend development.

### Running Migrations

To apply database migrations:

```bash
vanty dev migrate
```

You can pass additional options to the `migrate` command if needed.

### Creating a Superuser

To create a Django superuser:

```bash
vanty dev create-superuser
```

Follow the prompts to set up a new superuser for your application.

### Running Tests

To run tests for a specific Django app or file:

```bash
vanty dev run-tests <app_name> <file_name>
```

Replace `<app_name>` and `<file_name>` with appropriate values for your project.

### Additional Commands

- `vanty dev docs`: Open the documentation in a browser
- `vanty dev create_env`: Check for and create a .env file if needed
- `vanty dev build_container <container>`: Rebuild a specific Docker container
- `vanty dev stripe_cli`: Connect to Stripe CLI for webhook testing
- `vanty dev copy_statics`: Copy static files to the static directory
- `vanty dev run_admin <command>`: Run a Django admin command
