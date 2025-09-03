"""
WSGI config for rock_paper_scissors_project project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rock_paper_scissors_project.settings')

application = get_wsgi_application()
