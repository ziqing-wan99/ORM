import time
import os

try:
    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tpcc.settings')
    django.setup()
finally:
    pass

from tpcc.models import Items, Warehouses, Stocks

count = 0
start = time.time()

for _ in range(10):
    res = list(Stocks.objects.select_related('i_id').all())
    count += len(res)

elapsed_time = time.time() - start

# how many rows are inserted per second
print(f"Django, Rows/sec: { count / elapsed_time:10.2f}")

# Django, Rows/sec: [61766.71]
