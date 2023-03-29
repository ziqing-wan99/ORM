from sqlalchemy import Column, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects import mysql
import pymysql


pymysql.install_as_MySQLdb()
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Items(Base):
    # 表的名字:
    __tablename__ = 'items'

    # 表的结构:
    i_id = Column(mysql.INTEGER(), primary_key=True, autoincrement=True)
    i_im_id = Column(mysql.VARCHAR(8), nullable=False, unique=True)
    i_name = Column(mysql.VARCHAR(50), nullable=False)
    i_price = Column(mysql.DOUBLE(), nullable=False)

# 初始化数据库连接:
engine = create_engine(f"mysql://root:@localhost/tbench")
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# define table warehouses
class Warehouses(Base):
    __tablename__ = 'warehouses'
    w_id = Column(mysql.INTEGER(), primary_key=True, autoincrement=True)
    w_name = Column(mysql.VARCHAR(50), nullable=False)
    w_street = Column(mysql.VARCHAR(50), nullable=False)
    w_city = Column(mysql.VARCHAR(50), nullable=False)
    w_country = Column(mysql.VARCHAR(50), nullable=False)


# define table stocks
class Stocks(Base):
    __tablename__ = 'stocks'
    w_id = Column(mysql.INTEGER(), primary_key=True)
    i_id = Column(mysql.INTEGER(), primary_key=True)
    s_qty = Column(mysql.INTEGER())


Base.metadata.create_all(engine)