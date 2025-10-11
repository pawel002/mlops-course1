import os
import yaml
import argparse
from dotenv import load_dotenv
from settings import Settings
from constants import SECRETS_PATH


def export_envs(environment: str = "dev"):
    return load_dotenv(f"./config/.env.{environment}")


def load_secrets(path):
    def to_env_name(key):
        return key.replace("-", "_").replace(" ", "_").upper()

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    for key, value in data.items():
        # we accept only first degree variables, no nesting
        if not isinstance(key, str) or not isinstance(value, str):
            continue

        env_key = to_env_name(key)
        os.environ[env_key] = value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    load_secrets(SECRETS_PATH)
    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API-KEY: ", settings.API_KEY)
