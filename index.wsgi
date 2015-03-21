import sys
import os.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'supermilai.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'supermilai'))

import sae
from supermilai import wsgi

application = sae.create_wsgi_app(wsgi.application)