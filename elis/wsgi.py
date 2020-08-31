import os, sys

sys.path.append('/home/theraasch/apps_wsgi')

sys.path.append('/home/theraasch/apps_wsgi/elis')

os.environ['DJANGO_SETTINGS_MODULE'] = 'elis.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
