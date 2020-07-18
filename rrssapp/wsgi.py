"""
WSGI config for rrssapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import django


from django.core.wsgi import get_wsgi_application

# For heroku

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rrssapp.settings')
django.setup()
application = get_wsgi_application()
