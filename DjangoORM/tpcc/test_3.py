import time
import os
import random

try:
    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tpcc.settings')
    django.setup()
finally:
    pass

from django.db import transaction
from tpcc.models import Items, Warehouses, Stocks

# insert 2000 rows, all rows are inserted in a db session
rows_count = 4000
count = 0

start = time.time()
with transaction.atomic():
    while count < rows_count:
        w_id = random.randint(1, 2000)
        i_id = random.randint(1, 2000)
        warehouse = Warehouses.objects.filter(w_id=w_id).all()[0]
        item = Items.objects.filter(i_id=i_id).all()[0]
        if Stocks.objects.filter(w_id=w_id, i_id=i_id).exists():
            continue
        count = count + 1
        s_id = count
        Stocks.objects.create(s_id=s_id, w_id=warehouse, i_id=item, s_qty=random.randint(0, 100))

elapsed_time = time.time() - start

# how many rows are inserted per second
print(f"Django, Rows/sec: { rows_count / elapsed_time:10.2f}")

# Django, Rows/sec: [382.3]
