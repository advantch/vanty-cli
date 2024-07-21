
## Auth

The `vanty auth` module manages authentication tokens and user sessions.

### Setting a License Token

To set a license token:

```bash
vanty auth set <license-token>
```

This verifies the token and stores it in the configuration file.

### Removing a Token

To remove the stored token:

```bash
vanty auth remove
```

### Logging In

To log in and obtain an authentication token:

```bash
vanty auth login
```

You will be prompted for your username and password.

### Logging Out

To log out and remove the authentication token:

```bash
vanty auth logout
```

### Checking Authentication Status

To display your current authentication status:

```bash
vanty auth status
```
