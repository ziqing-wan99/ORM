import random
import time
from schema import *
from sqlalchemy.orm import sessionmaker


# insert 4000 rows, each row is inserted in a db session
rows_count = 4000
start = time.time()
Session = sessionmaker(bind=engine)
session = Session()
check_set = set()

while len(check_set) < rows_count:
    warehouses = session.query(Warehouses.w_id).filter_by(w_id=random.randint(1, 200))
    items = session.query(Items.i_id).filter_by(i_id=random.randint(1, 200))
    check_set.add((warehouses.first()[0], items.first()[0]))


for warehouses, items in check_set:
    new_entry = Stocks(w_id=warehouses, i_id=items, s_qty=random.randint(0, 100))
    session.add(new_entry)
session.commit()
elapsed_time = time.time() - start

# Not the exact time
print(f"SQLAlchemy ORM, Rows/sec: {rows_count / elapsed_time: 10.2f}")
# SQLAlchemy ORM, Rows/sec:    799.66
