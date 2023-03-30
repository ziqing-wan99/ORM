import time
from itertools import count

from schema import *
from peewee import *


# Select w.w_id, w.w_name, s.s_qty from the Warehouses and Stocks tables
start = time.time()


query = (Warehouses
         .select(Warehouses.w_id, Warehouses.w_name, Stocks.s_qty)
         .join(Stocks)
         .dicts())


elapsed_time = time.time() - start

# PeeweeORM, Rows/sec:    287882.00
for row in query:
    print(row)

# how many rows are selected per second
print(f"PeeweeORM, Rows/sec: {len(query) / elapsed_time:10.2f}")