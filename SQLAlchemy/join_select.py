import time
from schema import *
from sqlalchemy.orm import sessionmaker

# Select w.w_id, w.w_name, s.s_qty from the Warehouses and Stocks tables
rows_count = 0
start = time.time()
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Warehouses.w_id, Warehouses.w_name, Stocks.s_qty).join(Stocks, Warehouses.w_id == Stocks.w_id)
res = query.all()
rows_count = len(res)

elapsed_time = time.time() - start
# how many rows are selected per second
print(f"SQLAlchemy ORM, Rows/sec: {rows_count / elapsed_time: 10.2f}")
# SQLAlchemy ORM, Rows/sec:   65570.58
