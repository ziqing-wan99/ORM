import time
from schema import *
from sqlalchemy.orm import sessionmaker

# select rows from Items with i_price<50
rows_count = 0
start = time.time()
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Items)
res = query.filter(Items.i_id < 19000).all()
elapsed_time = time.time() - start
rows_count = len(res)
# how many rows are selected per second
print(f"Test 9 SQLAlchemy ORM, Rows/sec: {rows_count / elapsed_time: 10.2f}")
# SQLAlchemy ORM, Rows/sec:   39139.94

