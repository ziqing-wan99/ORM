import time
import os

try:
    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tpcc.settings')
    django.setup()
finally:
    pass

from tpcc.models import Items, Warehouses, Stocks
from django.db import transaction

count = 0
start = time.time()

objs = list(Stocks.objects.all())
count = len(objs)

with transaction.atomic():
    for obj in objs:
        obj.delete()

elapsed_time = time.time() - start

# how many rows are inserted per second
print(f"Django, Rows/sec: { count / elapsed_time:10.2f}")

# Django, Rows/sec: [2171.93]
