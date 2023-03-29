import time

from schema import *
from pony.orm import select, db_session

# Select from Items where i_id <19000
rows_count = 0
start = time.time()

with db_session():
    res = list(select(x for x in Items if x.i_id < 19000))
    rows_count += len(res)

elapsed_time = time.time() - start
# how many rows are selected per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")

