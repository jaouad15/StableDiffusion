# test_stablediffusion.py
"""
Tests for StableDiffusion module.
"""

import unittest
from stablediffusion import StableDiffusion

class TestStableDiffusion(unittest.TestCase):
    """Test cases for StableDiffusion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StableDiffusion()
        self.assertIsInstance(instance, StableDiffusion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StableDiffusion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
