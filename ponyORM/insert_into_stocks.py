import random
import time

from schema import *
from pony.orm import commit, db_session


# insert 4000 rows, each row is inserted in a db session
rows_count = 4000
start = time.time()
i=0
while i < rows_count:
    with db_session():
        warehouse = Warehouses.get(w_id=random.randint(1, 2000))
        item = Items.get(i_id=random.randint(1, 2000))
        if Stocks.exists(w_id=warehouse, i_id=item):
            continue
        Stocks(w_id=warehouse, i_id=item, s_qty=random.randint(0, 100))
        i = i+1
        commit()

elapsed_time = time.time() - start
# how many rows are inserted per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")
# PonyORM, Rows/sec:    3169.60
