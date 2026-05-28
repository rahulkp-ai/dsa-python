"""Root conftest.py — ensure src is on path for all tests."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
