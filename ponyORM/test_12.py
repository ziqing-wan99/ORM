import time

from schema import *
from pony.orm import select, db_session, commit

# Update i_name from Items
start = time.time()

with db_session():
    res = list(select(x for x in Items))
    rows_count = len(res)
    for r in res:
        r.i_name = f"ItemNameUpdated{r.i_id}"
    commit()

elapsed_time = time.time() - start
# how many rows are updated per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")

