import io
import pytest
import respx
import httpx
from vanty._client import Client
from vanty.schema import LicenseVerifiedHttpResponse, DownloadProjectHttpResponse, ProfileStatus

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def mock_config(mocker):
    mock = mocker.patch('vanty._client.config')
    mock.get.return_value = "https://www.advantch.com/api/v1"
    return mock


def test_download_zip(client, respx_mock):
    respx_mock.get("https://example.com/test.zip").mock(return_value=httpx.Response(200, content=b"Test zip content"))
    result = client._download_zip("https://example.com/test.zip")
    assert isinstance(result, io.BytesIO)
    assert result.getvalue() == b"Test zip content"

def test_verify_success(client, mock_config, respx_mock):
    respx_mock.get("https://www.advantch.com").mock(return_value=httpx.Response(200))
    respx_mock.post("https://www.advantch.com/api/v1/projects/authenticate-license/").mock(
        return_value=httpx.Response(200, json={
            "is_valid": True,
            "token_id": "test_token_id",
            "token_secret": "test_token_secret",
            "license_id": "test_license_id"
        })
    )

    result = client.verify("test_license_token")
    assert isinstance(result, LicenseVerifiedHttpResponse)
    assert result.is_valid, result
    assert result.token_id == "test_token_id"
    assert result.token_secret == "test_token_secret"

def test_verify_failure(client, mock_config, respx_mock):
    respx_mock.get("https://www.advantch.com").mock(return_value=httpx.Response(200))
    respx_mock.post("https://www.advantch.com/api/v1/projects/authenticate-license/").mock(
        return_value=httpx.Response(400, json={"error": "Invalid token"})
    )
    result = client.verify("invalid_license_token")
    assert isinstance(result, LicenseVerifiedHttpResponse)
    assert not result.is_valid

def test_download_success(client, mock_config, mocker, respx_mock):
    # mock zipfile.ZipFile
    respx_mock.get("https://www.advantch.com").mock(return_value=httpx.Response(200))
    m = mocker.patch('zipfile.ZipFile')
    respx_mock.get("https://www.advantch.com/api/v1/projects/download/").mock(
        return_value=httpx.Response(200, json={
                "is_valid": True,
                "profile_status": "active",
                "url": "https://example.com/project.zip",
                "project_id": "test_project",
                "version": "1.0.0",
                "profile_id": "test_profile"
            })
        )
    respx_mock.get("https://example.com/project.zip").mock(
        return_value=httpx.Response(200, content=b"Project zip content")
    )
    mocker.patch('zipfile.ZipFile.extractall')
    client.download("test_project")
    # Assert that ZipFile.extractall was called
        