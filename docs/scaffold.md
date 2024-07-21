
## Scaffold Module Usage

The `vanty scaffold` module allows developers to quickly generate new Django apps using custom templates.

### Creating a New Django App

To scaffold a new Django app:

```bash
vanty scaffold startapp <app_name>
```

By default, the app will be created in the `apps` directory of your Django project.

This will include example models, views, schema for `Django Ninja` and api.

### Specifying a Custom Template

To use a custom template for your new app:

```bash
vanty scaffold startapp <app_name> --template-url <template_url>
```

Replace `<template_url>` with the URL of your custom template.

### Overriding the Destination Directory

To change the destination directory for the new app:

```bash
vanty scaffold startapp <app_name> --destination <destination_path>
```

### Overriding the Manage.py Check

To bypass the check for `manage.py` in the current working directory:

```bash
vanty scaffold startapp <app_name> --override
```
