import time

from schema import *
from pony.orm import select, db_session, distinct

# select rows from Items with i_price<50
rows_count = 0
start = time.time()

with db_session():
    res = list(select(distinct(i.i_price) for i in Items))
    # res = list(select(i.i_price for i in Items))

    rows_count += len(res)
    print(rows_count)

elapsed_time = time.time() - start
# how many rows are selected per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")
# PonyORM, Rows/sec:   64268.39

