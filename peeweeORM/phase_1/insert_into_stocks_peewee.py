import random
import time

from schema import *
from peewee import *


# insert 4000 rows, each row is inserted in a db session
rows_count = 4000
start = time.time()

i = 0
while i < rows_count:
    warehouse = Warehouses.get(w_id=random.randint(1, 200))
    item = Items.get(i_id=random.randint(1, 200))
    if Stocks.select().where(Stocks.w_id == warehouse, Stocks.i_id == item).exists():
        continue
    Stocks.create(w_id=warehouse, i_id=item, s_qty=random.randint(0, 100))
    i = i + 1

elapsed_time = time.time() - start
# how many rows are inserted per second
print(f"PeeweeORM, Rows/sec: {rows_count / elapsed_time:10.2f}")
