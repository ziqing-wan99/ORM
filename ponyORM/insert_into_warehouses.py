import time

from schema import *
from pony.orm import commit, db_session


# insert 2000 rows, each row is inserted in a db session
rows_count = 2000
start = time.time()

for i in range(rows_count):
    with db_session():
        w_id = i+1
        w_name = f"warehouse{w_id}"
        w_street = f"street of {w_name}"
        w_city = f"city of {w_name}"
        w_country = f"country of {w_name}"
        Warehouses(w_id=w_id, w_name=w_name, w_street=w_street, w_city=w_city, w_country=w_country)
        commit()

elapsed_time = time.time() - start
# how many rows are inserted per second
print(f"PonyORM, Rows/sec: {rows_count / elapsed_time:10.2f}")
# PonyORM, Rows/sec:    5420.94
