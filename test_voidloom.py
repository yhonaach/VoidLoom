# test_voidloom.py
"""
Tests for VoidLoom module.
"""

import unittest
from voidloom import VoidLoom

class TestVoidLoom(unittest.TestCase):
    """Test cases for VoidLoom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VoidLoom()
        self.assertIsInstance(instance, VoidLoom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VoidLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
