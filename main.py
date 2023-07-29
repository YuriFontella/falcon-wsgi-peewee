import os, uvicorn

app = 'server.www:app'
app_dir = os.path.abspath(os.path.dirname(__file__))
host = '0.0.0.0'
port = 8000
workers = 4
log_level = 'debug'

reload = True

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port, log_level=log_level, workers=workers, reload=False)