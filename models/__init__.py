#!/usr/bin/python3
"""
    This if __init__ file to create a unique FileStorage instance
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
