"""
Unit and regression test for the pbj package.
"""

# Import package, test suite, and other packages as needed
import pbj
import pytest
import sys

def test_pbj_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "pbj" in sys.modules
