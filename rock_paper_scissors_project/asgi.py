"""
ASGI config for rock_paper_scissors_project project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rock_paper_scissors_project.settings')

application = get_asgi_application()
