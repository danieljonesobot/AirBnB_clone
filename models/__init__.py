#!/usr/bin/python3
""" This module reload from json to dict
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
