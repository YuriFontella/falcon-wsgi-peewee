import multiprocessing, os

from config.migrations.main import create_tables

bind = '0.0.0.0:8000'
workers = int(multiprocessing.cpu_count() / 2) + 1
wsgi_app = 'server.main:app'
loglevel = 'info'
chdir=os.path.dirname(os.path.abspath(__file__))
timeout=300
limit_request_line=8188

reload = True

def when_ready(server):
    create_tables()