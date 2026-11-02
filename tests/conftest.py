import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def create_results_folder():
    os.makedirs("test-results", exist_ok=True)