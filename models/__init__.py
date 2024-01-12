#!/usr/bin/python3
"""
    This if __init__ file to create a unique FileStorage instance
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
