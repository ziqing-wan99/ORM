import time
from schema import *
from sqlalchemy.orm import sessionmaker


rows_count = 2000
start = time.time()
Session = sessionmaker(bind=engine)
session = Session()
# delete all rows from Stocks
rows_count = session.query(Stocks).count()
session.commit()

start = time.time()
session.query(Stocks).delete()
session.commit()

elapsed_time = time.time() - start
# how many rows are deleted per second
print(f"SQLAlchemy ORM, Rows/sec: {rows_count / elapsed_time: 10.2f}")
# SQLAlchemy ORM, Rows/sec:   170553.89
