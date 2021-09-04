#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config

def main():
    """Run administrative tasks."""
    mode = config("MODE", default="DEV")
    if mode == "DEV":
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "config.settings.development"
        )
    elif mode == "STAGING":
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "config.settings.staging"
        )
    else:
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "config.settings.production"
        )
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
