import time

from schema import *
from peewee import *

# select rows from Items with i_price<50
rows_count = 0
start = time.time()

with db.transaction():
    items = list(Items.select().where(Items.i_id < 10000))
    rows_count = items.count()

elapsed_time = time.time() - start
# how many rows are selected per second
print(f"PeeweeORM, Rows/sec: {rows_count / elapsed_time:10.2f}")