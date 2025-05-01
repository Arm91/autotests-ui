import pytest

SYSTEM_VERSION = "v1.2.0"


@pytest.mark.skipif(SYSTEM_VERSION != "v1.3.0", reason="Skipping this test for demonstration purposes")
def test_system_version_valid():
    pass


@pytest.mark.skipif(SYSTEM_VERSION == "v1.2.0", reason="Skipping this test for demonstration purposes")
def test_system_version_invalid():
    pass
