from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
DOTENV_PATH = BASE_DIR / ".env"

# Use utf-8-sig to tolerate BOM-prefixed .env files on Windows.
load_dotenv(dotenv_path=DOTENV_PATH, encoding="utf-8-sig")


def get_openai_api_key() -> str | None:
    value = os.getenv("OPENAI_API_KEY")
    return value.strip() if value else None


def get_openai_base_url() -> str | None:
    value = os.getenv("OPENAI_BASE_URL")
    return value.strip() if value else None


def get_openai_model() -> str:
    value = os.getenv("OPENAI_MODEL")
    return value.strip() if value else "gpt-4o-mini"


def require_openai_api_key() -> str:
    api_key = get_openai_api_key()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Please add it to your .env file.")
    return api_key
