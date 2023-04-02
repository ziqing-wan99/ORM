import time
from schema import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

# select rows from Items with i_price<50
rows_count = 0
start = time.time()
Session = sessionmaker(bind=engine)
session = Session()

res = session.query(Stocks.w_id, func.count(Stocks.w_id)).filter(Stocks.w_id < 1000).group_by(Stocks.w_id).all()
elapsed_time = time.time() - start
rows_count = len(res)
# how many rows are selected per second
print(f"Test 10 SQLAlchemy ORM, Rows/sec: {rows_count / elapsed_time: 10.2f}")
# SQLAlchemy ORM, Rows/sec:   17403.75

