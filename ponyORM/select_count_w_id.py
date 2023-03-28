import time

from schema import *
from pony.orm import select, db_session, distinct, count
from pony.orm import *
# select rows from Items with i_price<50
rows_count = 0
start = time.time()

with db_session():
    res = select((s.w_id, count(s.s_qty)) for s in Stocks if s.w_id.w_id < 1000)
    rows_count += len(res)
    print(res[:])

elapsed_time = time.time() - start
# how many rows are selected per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")
# PonyORM, Rows/sec:   64268.39

