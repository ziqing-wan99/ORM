import time
from schema import *
from sqlalchemy.orm import sessionmaker


# insert 2000 rows, each row is inserted in a db session
rows_count = 2000
start = time.time()
Session = sessionmaker(bind=engine)
session = Session()

for i in range(rows_count):
    w_id = i+1
    w_name = f"warehouse{w_id}"
    w_street = f"street of {w_name}"
    w_city = f"city of {w_name}"
    w_country = f"country of {w_name}"
    new_entry = Warehouses(w_id=w_id, w_name=w_name, w_street=w_street, w_city=w_city, w_country=w_country)
    session.add(new_entry)
session.commit()

elapsed_time = time.time() - start
# how many rows are inserted per second
print(f"SQLAlchemy ORM, Rows/sec: {rows_count / elapsed_time: 10.2f}")
# SQLAlchemy ORM, Rows/sec:   7672.21
