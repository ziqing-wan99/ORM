import time
import os

try:
    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tpcc.settings')
    django.setup()
finally:
    pass

from django.db import transaction
from tpcc.models import Items, Warehouses, Stocks

# insert 20000 rows, all rows are inserted in a db session
rows_count = 20000

start = time.time()
with transaction.atomic():
    for i in range(rows_count):
        w_id = i + 1
        w_name = f"warehouse{w_id}"
        w_street = f"street of {w_name}"
        w_city = f"city of {w_name}"
        w_country = f"country of {w_name}"
        Warehouses.objects.create(w_id=w_id, w_name=w_name, w_street=w_street, w_city=w_city, w_country=w_country)

elapsed_time = time.time() - start

# how many rows are inserted per second
print(f"Django, Rows/sec: { rows_count / elapsed_time:10.2f}")

# Django, Rows/sec: [3263.18]
