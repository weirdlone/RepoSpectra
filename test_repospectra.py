# test_repospectra.py
"""
Tests for RepoSpectra module.
"""

import unittest
from repospectra import RepoSpectra

class TestRepoSpectra(unittest.TestCase):
    """Test cases for RepoSpectra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RepoSpectra()
        self.assertIsInstance(instance, RepoSpectra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RepoSpectra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
