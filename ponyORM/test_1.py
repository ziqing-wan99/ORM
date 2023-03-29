import random
import time

from schema import *
from pony.orm import commit, db_session

# insert 20000 rows into items in one db session
rows_count = 20000
start = time.time()

with db_session():
    for i in range(rows_count):
        i_id = i + 1
        i_im_id = f"Im{i_id}"
        i_name = f"ItemName{i_id}"
        i_price = round(random.uniform(1, 99), 4)  # a random floating-point number between 1 and 99 (4 decimal places)
        Items(i_id=i_id, i_im_id=i_im_id, i_name=i_name, i_price=i_price)
    commit()
elapsed_time = time.time() - start
# how many rows are inserted per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")
