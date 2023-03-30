import time

from schema import *
from peewee import *

# update i_name of all rows from Items
start = time.time()

with db.transaction():
    rowscount = Items.update(i_name='ItemNameUpdated' + Items.i_name).execute()
    db.commit()

elapsed_time = time.time() - start
# how many rows are updated per second
print(f"PeeweeORM, Rows/sec: {rowscount / elapsed_time:10.2f}")

