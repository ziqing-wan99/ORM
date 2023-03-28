from django.db import models


# Create your models here.
class Items(models.Model):
    i_id = models.IntegerField(primary_key=True)
    i_im_id = models.CharField(max_length=8, unique=True)
    i_name = models.CharField(max_length=50)
    i_price = models.FloatField()


class Warehouses(models.Model):
    w_id = models.IntegerField(primary_key=True, auto_created=True)
    w_name = models.CharField(max_length=50)
    w_street = models.CharField(max_length=50)
    w_city = models.CharField(max_length=50)
    w_country = models.CharField(max_length=50)


class Stocks(models.Model):
    s_id = models.IntegerField(primary_key=True, auto_created=True)
    w_id = models.ForeignKey(Warehouses, on_delete=models.CASCADE)
    i_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    s_qty = models.IntegerField()