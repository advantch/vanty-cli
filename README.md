# Vanty CLI

CLI for managing projects from advantch.com including:

- Vanty Starter Kit

   This  Vanty Starter Kit is the fastest way to launch new SaaS & AI products.

   Visit https://www.advantch.com/ for documentation and more information

## Installation

We recommend using pipx to install vanty-cli:

```bash
pipx install vanty-cli
```

## Usage

1. Verify your license:

   ```bash
   vanty verify --license <your-license-id>
   ```

2. Download the project to the current directory:

   ```bash
   vanty project download
   ```

3. Get started:

   ```bash
   cd <project-name>
   vanty dev init
   ```

4. Run the project:

   ```bash
    vanty dev run
    ```

## Issues & Support:

Advantch users can report issues on the slack issue channel.

- https://www.advantch.com/issues/

## PR and Contributions:

Please note that whilst this is open source, it is not intended to be a community project.

Advantch users can submit PRs for extensions etc that maybe helpful to the core project or other users.

Otherwise, please fork and use this as a base for your own projects.

<img alt="logo" height="20" width="20" src="https://cdn.advantch.com/static/images/logo.png">
