"""
WSGI config for blogplatform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

import django.core.wsgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogplatform.settings")

application = django.core.wsgi.get_wsgi_application()
