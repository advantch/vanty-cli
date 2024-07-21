## Tutorials

### Creating Your First Vanty Project

1. Install Vanty CLI
2. Authenticate with your license token
3. Download a starter project
4. Initialize the project
5. Run the project locally
6. Make your first changes

#### Detailed Steps

1. Install Vanty CLI using poetry as shown in the Installation section.

2. Authenticate your license:
   ```bash
   vanty auth verify <your-license-token>
   ```
   This will store your authentication token in the `~/.vanty.toml` file.

3. Download a starter project:
   ```bash
   vanty project download --project <project-id>
   ```
   Replace `<project-id>` with the ID of the project you want to use as a starting point.

4. Initialize the project:
   ```bash
   cd <project-name>
   vanty dev init
   ```
   This command will set up your development environment, including building Docker containers if required.

5. Start the project:
   ```bash
   vanty dev start
   ```
   This will start your development server and any associated services.

6. Make your first changes:
   - Open your project in your preferred code editor.
   - Modify files as needed.
   - Use `vanty dev` commands to manage your development workflow.
