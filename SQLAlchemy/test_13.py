import time
from schema import *
from sqlalchemy.orm import sessionmaker

# Select w.w_id, w.w_name, s.s_qty from the Warehouses and Stocks tables
rows_count = 0
start = time.time()
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Stocks, Warehouses).outerjoin(Warehouses, Warehouses.w_id == Stocks.w_id)
res = query.all()
rows_count = len(res)

elapsed_time = time.time() - start
# how many rows are selected per second
print(f"Test 13 SQLAlchemy ORM, Rows/sec: {rows_count / elapsed_time: 10.2f}")
# SQLAlchemy ORM, Rows/sec:   27163.25
