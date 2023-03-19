import time

from schema import *
from pony.orm import select, db_session, commit

# update i_name of all rows from Items
start = time.time()

with db.transaction():
    query = Items.update(name='ItemNameUpdated' + Items.i_name).execute()
    db.commit()

elapsed_time = time.time() - start
# how many rows are updated per second
print(f"PonyORM, Rows/sec: {query.rowscount / elapsed_time:10.2f}")
# PonyORM, Rows/sec:   14101.20

