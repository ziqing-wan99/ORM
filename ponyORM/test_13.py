import time
from itertools import count
from pony.orm import select, db_session
from ponyORM.schema import Warehouses

# Select from Stocks left join Warehouses
# Select w.w_id, w.w_name, s.s_qty from the Warehouses and Stocks tables
start = time.time()

with db_session():
    query = select((w.w_id, w.w_name, s.s_qty) for w in Warehouses for s in w.stocks)
    result = query[:]
    rows_count = len(result)

elapsed_time = time.time() - start
# how many rows are selected per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")
