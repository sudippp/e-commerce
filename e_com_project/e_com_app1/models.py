from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.IntegerField()
    mobile_number = models.IntegerField()

    def __str__(self):
        return str(self.id)



catagory_choice = [
    ("M","mobile"),
    ("L","laptop"),
]
class Product(models.Model):
    titel = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    catagory = models.CharField(max_length=10,choices=catagory_choice)
    product_img = models.ImageField(upload_to="product_img")

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

    @property
    def item_cost(self):
        return self.quantity * self.product.discount_price

status_choice = [
        ("Acepted","Acepted"),
        ("Packed","Packed"),
        ("On the way","On the way"),
        ("Delivered","Delivered"),
        ("Cancel","Cancel"),
    ]

payment_method_choice = [
        ("Cash on Delivery","Cash on Delivery"),
        ("UPI Payment","UPI Payment"),
        ("Net Banking","Net Banking"),
    ]
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100,default="Cash on Delivery",choices=payment_method_choice)
    status = models.CharField(max_length=50, default="Pending",choices=status_choice)

    @property
    def item_cost(self):
        return self.quantity * self.product.discount_price
    