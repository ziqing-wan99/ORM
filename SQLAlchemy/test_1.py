import random
import time
from schema import *
from sqlalchemy.orm import sessionmaker


# insert 2000 rows, each row is inserted in a db session
rows_count = 2000
start = time.time()
Session = sessionmaker(bind=engine)
session = Session()

for i in range(rows_count):
    i_id = i + 1
    i_im_id = f"Im{i_id}"
    i_name = f"ItemName{i_id}"
    i_price = round(random.uniform(1, 99), 4)  # a random floating-point number between 1 and 99 (4 decimal places)
    new_entry = Items(i_id=i_id, i_im_id=i_im_id, i_name=i_name, i_price=i_price)
    session.add(new_entry)
session.commit()
elapsed_time = time.time() - start

print(f"SQLAlchemy ORM, Rows/sec: {rows_count / elapsed_time: 10.2f}")
# SQLAlchemy ORM, Rows/sec:    11523.21
