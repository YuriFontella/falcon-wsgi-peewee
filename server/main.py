import os, uvicorn, multiprocessing, argparse

app = 'server.www:app'
app_dir = os.path.dirname(os.path.abspath(__file__))
host = '0.0.0.0'
port = 8000
workers = (2 * multiprocessing.cpu_count()) + 1

ssl_ca_certs = os.environ.get('SSL_CA')
ssl_keyfile = os.environ.get('SSL_KEY')

parser = argparse.ArgumentParser()

parser.add_argument('--reload', default=False)
parser.add_argument('--log-level', default='info')

parser.add_argument('--env', required=True)

args = parser.parse_args()

os.environ['ENV'] = args.env

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port, log_level=args.log_level, workers=workers, reload=args.reload, ssl_ca_certs=ssl_ca_certs, ssl_keyfile=ssl_keyfile)