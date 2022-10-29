#!/usr/bin/python3
"""This deserialises json file"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
