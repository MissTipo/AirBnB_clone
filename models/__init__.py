#!/usr/bin/python3
"""This deserialises json file"""

from models.engine.file_storage import FileStorage
import json

storage = FileStorage()
storage.reload()
