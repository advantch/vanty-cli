# Vanty CLI Documentation

## Overview

Vanty CLI is a powerful tool for managing projects from advantch.com, including The Starter Kit and Advantch Cloud (beta). It provides a set of commands to streamline your development workflow, from project initialization to deployment.

### Key Features

- Project initialization and management
- Development environment setup
- Database migrations
- Scaffolding new Django apps
- Authentication and token management
- Community package integration

### Installation

To install Vanty CLI, use poetry:

```bash
poetry install vanty
```

### Quick Start

1. Verify your license:

```bash
vanty auth verify <your-license-token>
```

2. Download a project:

```bash
vanty project download --project <project-id>
```

3. Initialize the project:

```bash
cd <project-name>
vanty dev init
```

4. Start the project:

```bash
vanty dev start
```

Next steps:

- [Development - Working on your project locally](./dev.md)
- [Scaffold - Creating a new app](./scaffold.md)
- [Auth - Managing your authentication](./auth.md)
- [Config - Configuration](./config.md)
- [Tutorials - Tutorials](./tutorials.md)