from unittest.mock import patch

from typer.testing import CliRunner

from vanty._client import Client
from vanty.cli import app

runner = CliRunner()


@patch("zipfile.ZipFile.extractall")
def test_download_success(mock_extract, mocked_api):
    client = Client()
    client.download("test_project")

    assert mock_extract.called
    assert (
        "Project files downloaded successfully"
        in runner.invoke(app, ["download"]).output
    )
