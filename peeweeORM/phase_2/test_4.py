import random
import time

from schema import *
from peewee import *

# insert 2000 rows, all rows are inserted in a db session
rows_count = 20000
start = time.time()

for i in range(rows_count):
    with db.transaction():
        i_id = i + 1
        i_im_id = f"Im{i_id}"
        i_name = f"ItemName{i_id}"
        i_price = round(random.uniform(1, 99), 4)  # a random floating-point number between 1 and 99 (4 decimal places)
        Items.create(i_id=i_id, i_im_id=i_im_id, i_name=i_name, i_price=i_price)
        db.commit()

elapsed_time = time.time() - start
# how many rows are inserted per second
print(f"PeeweeORM, Rows/sec: {rows_count / elapsed_time:10.2f}")