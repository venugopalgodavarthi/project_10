from django.db import models

# Create your models here.


class menu_items(models.Model):
    mid = models.SmallAutoField(primary_key=True)
    i_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.i_name


class food_items(models.Model):
    fid = models.BigAutoField(primary_key=True)
    mid = models.ForeignKey(menu_items, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50)
    f_desc = models.TextField()
    f_quantity = models.PositiveIntegerField(default=1)
    f_price = models.PositiveIntegerField(default=30)
    discount = models.PositiveSmallIntegerField(default=0)
    f_img = models.ImageField()


class cart_items(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cust_id = models.IntegerField()
    food_id = models.IntegerField()


class order_food(models.Model):
    oid = models.AutoField(primary_key=True)
    cust_id = models.PositiveIntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.PositiveBigIntegerField()
    address = models.TextField()
    shipping_address = models.BooleanField()
    country = models.CharField(max_length=30, choices=[
                               ['India', 'India'], ['USA', 'USA'], ['UK', 'UK']])
    states = models.CharField(max_length=30, choices=[['AP', 'AP'], [
                              'TS', 'TS'], ['SR', 'SR'], ['TN', 'TN']])
    pincode = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now=True)
    total_price = models.FloatField()
    


class order_food_items(models.Model):
    oid = models.ForeignKey(order_food, on_delete=models.CASCADE)
    food_id = models.PositiveIntegerField()
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
