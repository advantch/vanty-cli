import responses
import rich
from typer.testing import CliRunner
import os
from vanty.cli import app
from vanty.config import Config

os.environ["VANTY_CONFIG_PATH"] = "~/.vanty-test.toml"
runner = CliRunner()
config = Config()


@responses.activate
def test_auth_commands(mocker):
    auth_url = config.get("server_url") + "/projects/authenticate-license/"
    rich.print(auth_url)
    responses.add(
        responses.POST,
        auth_url,
        json={
            "is_valid": True,
            "token_id": "test_token_id",
            "token_secret": "test_token_secret",
        },
        status=200,
    )
    result = runner.invoke(app, ["auth", "set", "test_license_id"])

    assert "Token verified successfully" in result.output
    print(result.output)
    # check config
    token = config.get("token_id")
    assert token == "test_token_id"

    # remove token
    result = runner.invoke(app, ["auth", "remove"])
    assert "Token removed from" in result.output
