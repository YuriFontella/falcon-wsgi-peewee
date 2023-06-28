from playhouse.pool import PooledPostgresqlDatabase

db = PooledPostgresqlDatabase(user='postgres', password='123456', host='localhost', database='blocks', max_connections=8, stale_timeout=300)
