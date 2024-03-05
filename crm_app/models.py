from django.db import models

# Create your models here.

from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

class Opportunity(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.CharField(max_length=50)
    close_date = models.DateField()

class Interaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)
    date = models.DateTimeField()
    notes = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField()


class Contact(models.Model):
    Name = models.CharField(blank=True, null=True,max_length=555)
    Email = models.EmailField(blank=True, null=True)
    Mobile_Number = models.CharField(blank=True, null=True, max_length=15)
    Website_Url = models.URLField( blank=True, null=True,)
    Page_Url = models.URLField(blank=True, null=True,)
    Date = models.CharField(blank=True, null=True,max_length=15)
    Time = models.CharField(blank=True, null=True,max_length=15)
    Lead_ID = models.CharField(blank=True, null=True,max_length=50)
    Referral_information_field = models.TextField(blank=True, null=True,)
    Visitor_came_from = models.CharField(blank=True, null=True,max_length=100)
    utm_source = models.CharField(blank=True, null=True,max_length=50)
    utm_medium = models.CharField(blank=True, null=True,max_length=50)
    utm_campaign = models.CharField(blank=True, null=True,max_length=50)
    Last_visited_pages = models.TextField(blank=True, null=True,)
    

