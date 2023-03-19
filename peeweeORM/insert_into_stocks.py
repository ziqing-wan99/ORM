import random
import time

from schema import *
from peewee import *


# insert 4000 rows, each row is inserted in a db session
rows_count = 4000
start = time.time()

for i in range(rows_count):
    with db.transaction():
        warehouse = Warehouses.get(w_id=random.randint(1, 200))
        item = Items.get(i_id=random.randint(1, 200))
        if Stocks.exists(w_id=warehouse, i_id=item):
            continue
        Stocks.create(w_id=warehouse, i_id=item, s_qty=random.randint(0, 100))
        db.commit()

elapsed_time = time.time() - start
# how many rows are inserted per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")
# PeeweeORM, Rows/sec:    3169.60
