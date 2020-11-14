# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

try:
    ENVIRONMENT = os.environ['ENV']  # dev or prod
except KeyError:
    ENVIRONMENT = 'prod'


try:
    # Import static configurations.
    from .common import *
except ImportError:
    pass

print(f"\n\nENVIRNMOENTS: {os.environ}\n\n")


print(f"ENV: {os.environ.get('ENV')}")
print(f"SECRET_KEY: {os.environ.get('SECRET_KEY')}")


if ENVIRONMENT == 'prod':
    try:
        # Import prod environment configurations.
        from .production import *
    except ImportError:
        print('Import error on load prod environment configurations.')
elif ENVIRONMENT == 'dev':
    try:
        # Import dev environment configurations.
        from .develop import *
    except ImportError:
        print('Import error on load dev environment configurations.')
else:
    print("Select one environment on settings.py (ENVIRONMENT={'prod', 'dev'}).")

