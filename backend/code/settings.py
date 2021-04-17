import os

if 'DJANGO_SETTINGS' in os.environ:
    if os.environ['DJANGO_SETTINGS'] == "dev":
        from .customization.dev import *
else:
    from .customization.prod import *
