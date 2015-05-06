#!/usr/bin/env python
import os
import sys
import environ
import dotenv

ROOT_DIR = environ.Path(__file__) - 1  # (/a/b/myfile.py - 3 = /)

# Read key, value from .env file and load them into environment variable
# Useful to override your local or production settings, that should
# not be in version control.
dotenv.load_dotenv(str(ROOT_DIR.path('.env')))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
