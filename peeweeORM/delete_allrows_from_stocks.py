import time
from schema import *
from peewee import *

# delete all rows from Stocks
start = time.time()

rows = Stocks.delete().execute()


elapsed_time = time.time() - start
# how many rows are deleted per second
print(f"PeeweeORM, Rows/sec: {rows / elapsed_time:10.2f}")
