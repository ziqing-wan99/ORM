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

objs = list(Items.objects.all())
count = len(objs)

with transaction.atomic():
    for obj in objs:
        obj.i_name = f"{obj.i_name} Update"
        obj.save()

elapsed_time = time.time() - start

# how many rows are inserted per second
print(f"Django, Rows/sec: { count / elapsed_time:10.2f}")

# Django, Rows/sec: [1966.20]
