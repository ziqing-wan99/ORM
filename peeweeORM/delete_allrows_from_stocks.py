import time
from schema import *
from pony.orm import db_session, commit, delete, count

# delete all rows from Stocks
start = time.time()

query = Stocks.delete().execute()


elapsed_time = time.time() - start
# how many rows are deleted per second
print(f"PonyORM, Rows/sec: {query.rowcount / elapsed_time:10.2f}")
# PonyORM, Rows/sec:   14272.87
