import httpx
from typer.testing import CliRunner
import os
from vanty.cli import app
from vanty.config import Config

os.environ["VANTY_CONFIG_PATH"] = "~/.vanty-test.toml"
runner = CliRunner()
config = Config()


def test_auth_commands(mocker, respx_mock):
    auth_url = config.get("server_url") + "/projects/authenticate-license/"
    respx_mock.post(auth_url).mock(
        return_value=httpx.Response(
            200,
            json={
                "is_valid": True,
                "token_id": "test_token_id",
                "token_secret": "test_token_secret",
                "license_id": "test_license_id",
            },
        )
    )
    result = runner.invoke(app, ["auth", "set", "test_license_id"])

    assert "Token verified successfully" in result.output, result.output
    # check config
    import time

    time.sleep(2)
    token = config.get("token_id")
    assert token == "test_token_id"

    # remove token
    result = runner.invoke(app, ["auth", "remove"])
    assert "Token removed from" in result.output
