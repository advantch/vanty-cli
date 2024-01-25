## Vanty CLI - Scaffold Module Usage

The `vanty` CLI tool includes a `scaffold` module that allows developers to quickly generate new Django apps using a custom template. Here's how to use the `vanty scaffold` commands.

### Creating a New Django App

To scaffold a new Django app, run:

```bash
vanty scaffold startapp <app_name>
```

Replace `<app_name>` with the desired name for your new app. By default, the app will be created in the `apps` directory of your Django project.

### Specifying a Custom Template

If you want to use a custom template for your new app, you can specify a template URL:

```bash
vanty scaffold startapp <app_name> --template-url <template_url>
```

Replace `<template_url>` with the URL of your custom template.

### Overriding the Destination Directory

To change the destination directory where the new app will be created, use:

```bash
vanty scaffold startapp <app_name> --destination <destination_path>
```

Replace `<destination_path>` with the path to your desired destination directory.

### Overriding the Manage.py Check

If you need to override the check for `manage.py` in the current working directory, use the `--override` flag:

```bash
vanty scaffold startapp <app_name> --override
```

This will bypass the check and allow you to run the command from a different directory.

### Additional Information

The `scaffold` module is designed to streamline the process of setting up new Django apps within your project. For more detailed information and options, use `vanty scaffold --help`.
