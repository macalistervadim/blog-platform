"""
ASGI config for blogplatform project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

import django.core.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogplatform.settings")

application = django.core.asgi.get_asgi_application()
