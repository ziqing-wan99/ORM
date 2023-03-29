import time

from schema import *
from pony.orm import *

# Select w_id, sum(quantity)  from Stocks where w_id<1000 group by w_id
rows_count = 0
start = time.time()

with db_session():
    res = select((s.w_id, sum(s.s_qty)) for s in Stocks if s.w_id.w_id < 1000)
    rows_count += len(res)
    print(res[:])

elapsed_time = time.time() - start
# how many rows are selected per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")
# PonyORM, Rows/sec:   64268.39

