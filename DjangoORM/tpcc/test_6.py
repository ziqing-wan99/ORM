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
    res = list(Items.objects.order_by('i_price').values_list('i_price', flat=True).distinct())
    count += len(res)

elapsed_time = time.time() - start

# how many rows are inserted per second
print(f"Django, Rows/sec: { count / elapsed_time:10.2f}")

# Django, Rows/sec: [535901.46]