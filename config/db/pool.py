from playhouse.pool import PooledPostgresqlDatabase

db = PooledPostgresqlDatabase('blocks', user='postgres', password='123456', host='localhost', max_connections=8, stale_timeout=300)
