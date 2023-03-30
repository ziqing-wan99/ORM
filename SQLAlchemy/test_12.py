import time
from schema import *
from sqlalchemy.orm import sessionmaker

# update i_name of all rows from Items
start = time.time()
rows_count = 0
Session = sessionmaker(bind=engine)
session = Session()

res = session.query(Items).all()
rows_count = len(res)
for r in res:
    r.i_name = f"ItemNameUpdated{r.i_id}"
session.commit()


elapsed_time = time.time() - start
# how many rows are updated per second
print(f"SQLAlchemy ORM, Rows/sec: {rows_count / elapsed_time: 10.2f}")
# SQLAlchemy ORM, Rows/sec:   4078.49
