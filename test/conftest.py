from app import app

import pytest
from unittest.mock import patch


@pytest.fixture

def client():
    client = app.test_client()

    yield client

