import time

from schema import *
from peewee import *

# select rows from Items with i_price<50
rows_count = 0
start = time.time()

query = (Stocks
         .select(Stocks.w_id, fn.Sum(Stocks.s_qty))
         .where(Stocks.w_id < 1000)
         .group_by(Stocks.w_id))


rows_count = len(query)

elapsed_time = time.time() - start
# how many rows are selected per second
print(f"PeeweeORM, Rows/sec: {rows_count / elapsed_time:10.2f}")