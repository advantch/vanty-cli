# Configuration


The main configuration options are the API tokens: the token id and the token secret.
These can be configured in two ways:

1. By running the ``vanty token set`` command.
   This writes the tokens to ``.vanty.toml`` file in your home directory.
2. By setting the environment variables ``VANTY_TOKEN_ID`` and ``VANTY_TOKEN_SECRET``.
   This takes precedence over the previous method.

.vanty.toml
---------------

The ``.vanty.toml`` file is generally stored in your home directory.
It should look like this::

```toml
[default]
token_id = "vk-12345..."
token_secret = "vs-12345..."
```

You can create this file manually, or you can run the ``vanty token set ...``
command (see below).

Setting tokens using the CLI
----------------------------

You can set a token by running the command::

```bash
vanty token set \
  --token-id <token id> \
  --token-secret <token secret>
```

This will write the token id and secret to ``.vanty.toml``.

If the token id or secret is provided as the string ``-`` (a single dash),
then it will be read in a secret way from stdin instead.

Other configuration options
---------------------------

Other possible configuration options are:

* ``loglevel`` (in the .toml file) / ``VANTY_LOGLEVEL`` (as an env var).
  Defaults to ``WARNING``.
  Set this to ``DEBUG`` to see a bunch of internal output.
* ``logs_timeout`` (in the .toml file) / ``VANTY_LOGS_TIMEOUT`` (as an env var).
  Defaults to 10.
  Number of seconds to wait for logs to drain when closing the session,
  before giving up.
* ``automount`` (in the .toml file) / ``VANTY_AUTOMOUNT`` (as an env var).
  Defaults to True.
  By default, vanty automatically mounts modules imported in the current scope, that
  are deemed to be "local". This can be turned off by setting this to False.
* ``server_url`` (in the .toml file) / ``VANTY_SERVER_URL`` (as an env var).
  Defaults to ``https://www.advantch.com/api/v1``.
  Not typically meant to be used.

Meta-configuration
------------------

Some "meta-options" are set using environment variables only:

* ``VANTY_CONFIG_PATH`` lets you override the location of the .toml file,
  by default ``~/.vanty.toml``.
* ``VANTY_PROFILE`` lets you use multiple sections in the .toml file
  and switch between them. It defaults to "default".
"""
://til.simonwillison.net for a lot of the ideas on how to structure this.
