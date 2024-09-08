import os
import pytest
from vanty.config import Config, _SETTINGS

@pytest.fixture
def config():
    return Config()

def test_config_get_default(config):
    assert config.get("loglevel") == "WARNING"
    assert config.get("server_url") == "https://www.advantch.com/api/v1"
    assert config.get("package_manager") == "pnpm"

def test_config_get_from_env(config, monkeypatch):
    monkeypatch.setenv("VANTY_LOGLEVEL", "DEBUG")
    assert config.get("loglevel") == "DEBUG"

def test_config_get_from_user_config(config, tmp_path, monkeypatch):
    config_file = tmp_path / ".vanty.toml"
    config_file.write_text('[default]\ntoken_id = "test_token"')
    monkeypatch.setattr("vanty.config.user_config_path", str(config_file))
    
    # Reload the _user_config
    import vanty.config
    vanty.config._user_config = vanty.config._read_user_config()
    assert config.get("token_id") == "test_token"
    # change the frontend root in file
    config_file.write_text('[default]\ntoken_id = "test_token"\nfrontend_root = "test_frontend_root"')
    # Reload the _user_config
    import vanty.config
    vanty.config._user_config = vanty.config._read_user_config()

    assert config.get("token_id") == "test_token"
    assert config.get("frontend_root") == "test_frontend_root"
    
def test_config_get_priority(config, tmp_path, monkeypatch):
    # Set up environment variable
    monkeypatch.setenv("VANTY_LOGLEVEL", "INFO")
    
    # Set up user config file
    config_file = tmp_path / ".vanty.toml"
    config_file.write_text('[default]\nloglevel = "DEBUG"')
    monkeypatch.setattr("vanty.config.user_config_path", str(config_file))
    
    # Reload the _user_config
    import vanty.config
    vanty.config._user_config = vanty.config._read_user_config()
    
    # Environment variable should take precedence
    assert config.get("loglevel") == "INFO"

def test_config_get_nonexistent_key(config):
    with pytest.raises(KeyError):
        config.get("nonexistent_key")

def test_config_getitem(config):
    assert config["loglevel"] == config.get("loglevel")

def test_config_display(config):
    display = config.display()
    assert isinstance(display, dict)
    assert set(display.keys()) == set(_SETTINGS.keys())

def test_config_repr(config):
    repr_string = repr(config)
    assert isinstance(repr_string, str)
    assert "loglevel" in repr_string
    assert "server_url" in repr_string

def test_config_transform(config, monkeypatch):
    monkeypatch.setenv("VANTY_SSR_ENABLED", "true")
    assert config.get("ssr_enabled") is True
    
    monkeypatch.setenv("VANTY_SSR_ENABLED", "false")
    assert config.get("ssr_enabled") is False
