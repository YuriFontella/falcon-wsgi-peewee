import multiprocessing

bind = "0.0.0.0:8000"
workers = int(multiprocessing.cpu_count() / 2)