import pytest
from pydantic import ValidationError
from src.settings import Settings


def test_settings_from_env():
    s = Settings()
    assert s.ENVIRONMENT == "test"
    assert s.APP_NAME == "test_app"
    assert s.API_KEY == "test_api_key"


def test_invalid_environment_raises(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "staging")
    with pytest.raises(ValidationError) as exc:
        Settings()
    assert "ENVIRONMENT must be one of" in str(exc.value)
