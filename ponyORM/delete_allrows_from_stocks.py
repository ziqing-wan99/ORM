import time
from schema import *
from pony.orm import db_session, commit, delete, count

# delete all rows from Stocks
with db_session():
    rows_count = count(i for i in Items)

start = time.time()

with db_session():
    delete(i for i in Items)
    commit()

elapsed_time = time.time() - start
# how many rows are deleted per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")
# PonyORM, Rows/sec:   14272.87
