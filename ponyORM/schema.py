from pony.orm import Database, PrimaryKey, Required, Set

# database connection
db = Database()
db.bind(provider='mysql', host='localhost', user='root', passwd='Wzq171332', db='pony')


# define table items
class Items(db.Entity):
    i_id = PrimaryKey(int, auto=True)
    i_im_id = Required(str, unique=True, max_len=8)
    i_name = Required(str, max_len=50)
    i_price = Required(float)
    stocks = Set('Stocks')

    # check option is not supported by ponyORM
    @property
    def price(self):
        return self.i_price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0.")
        self.i_price = value


# define table warehouses
class Warehouses(db.Entity):
    w_id = PrimaryKey(int, auto=True)
    w_name = Required(str, max_len=50)
    w_street = Required(str, max_len=50)
    w_city = Required(str, max_len=50)
    w_country = Required(str, max_len=50)
    stocks = Set('Stocks')


# define table stocks
class Stocks(db.Entity):
    w_id = Required(Warehouses)
    i_id = Required(Items)
    s_qty = Required(int)

    @property
    def quantity(self):
        return self.s_qty

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Quantity must be greater than 0.")
        self.s_qty = value

    PrimaryKey(w_id, i_id)


db.generate_mapping(create_tables=True)
