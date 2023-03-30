from peewee import *

db = MySQLDatabase('mydatabase', user='root', password='', host='localhost', port=3306)

# define table items
class Items(Model):
    i_id = AutoField(primary_key=True)
    i_im_id = CharField(max_length=50, unique=True, null=False)
    i_name = CharField(max_length=50, null=False)
    i_price = DecimalField(max_digits=5, decimal_places=2, null=False, constraints=[Check('i_price > 0')])

    class Meta:
        database = db

# define table warehouses
class Warehouses(Model):
    w_id = PrimaryKeyField()
    w_name = CharField(max_length=10)
    w_street = CharField(max_length=20)
    w_city = CharField(max_length=20)
    w_country = CharField(max_length=9)

    class Meta:
        database = db

# define table stocks
class Stocks(Model):
    w_id = ForeignKeyField(Warehouses, backref='stocks')
    i_id = ForeignKeyField(Items, backref='stocks')
    s_qty = SmallIntegerField()

    class Meta:
        primary_key = CompositeKey('w_id', 'i_id')
        database = db

# create the table if it does not exist
if not Items.table_exists():
    Items.create_table()

if not Warehouses.table_exists():
    Warehouses.create_table()

if not Stocks.table_exists():
    Stocks.create_table()
