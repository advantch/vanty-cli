## Configuration

Vanty CLI uses a configuration file to manage various settings and options. Understanding and properly configuring these options is crucial for efficient use of the CLI.

### Configuration File Location

The primary configuration file is located at:

```
~/.vanty.toml
```

This file is automatically created when you first use the CLI or can be manually created if needed.

### Configuration Options

Here are the key configuration options available in the `.vanty.toml` file:

1. `token_id`: Your Vanty authentication token ID
2. `token_secret`: Your Vanty authentication token secret
3. `server_url`: The API server URL (default: https://www.advantch.com/api/v1)
4. `loglevel`: Logging level (default: WARNING)
5. `package_manager`: Package manager to use (default: pnpm)
6. `use_docker`: Whether to use Docker for development (default: True)

### Setting Configuration Options

There are multiple ways to set these configuration options:

1. **Using the CLI**:
   You can set the token using the `vanty auth set` command:
   ```bash
   vanty auth set --token-id <your-token-id> --token-secret <your-token-secret>
   ```

2. **Editing the .vanty.toml file**:
   You can manually edit the `.vanty.toml` file. Here's an example of what it might look like:
   ```toml
   [default]
   token_id = "vk-12345..."
   token_secret = "vs-12345..."
   server_url = "https://www.advantch.com/api/v1"
   loglevel = "INFO"
   package_manager = "pnpm"
   frontend_root = "."
   use_docker = true
   ```

3. **Using Environment Variables**:
   You can set configuration options using environment variables. These take precedence over the `.vanty.toml` file. The environment variables are prefixed with `VANTY_`. For example:
   ```bash
   export VANTY_TOKEN_ID="your-token-id"
   export VANTY_TOKEN_SECRET="your-token-secret"
   export VANTY_SERVER_URL="https://custom-server.com/api/v1"
   ```

### Configuration Profiles

The `.vanty.toml` file supports multiple configuration profiles. The default profile is named "default", but you can create additional profiles for different environments or projects.

To create a new profile, add a new section to your `.vanty.toml` file:

```toml
[default]
token_id = "vk-12345..."
token_secret = "vs-12345..."

[development]
token_id = "vk-67890..."
token_secret = "vs-67890..."
server_url = "https://dev.advantch.com/api/v1"
```

To use a specific profile, you can set the `VANTY_PROFILE` environment variable:

```bash
export VANTY_PROFILE="development"
```

### Viewing Current Configuration

To view your current configuration settings, you can use the `vanty admin show-config` command:

```bash
vanty admin show-config
```

This will display all the current configuration settings, helping you verify your setup.

### Configuration Best Practices

1. **Security**: Never commit your `.vanty.toml` file to version control if it contains sensitive information like token secrets.
2. **Environment-specific configs**: Use different profiles for different environments (development, staging, production).
3. **Version control**: Consider using a `.vanty.toml.example` file in your version control, with sensitive information removed, as a template for other developers.
4. **Regular updates**: Periodically review and update your configuration, especially after Vanty CLI updates.

By properly configuring Vanty CLI, you can customize its behavior to best suit your development workflow and project requirements.
