from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f" {self.name} | {self.region}"


class Category(models.Model):
    name =models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
   

class Repair(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
   

class Currency(models.Model):
    value_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.value_name

    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.user}"


class Rating(models.Model):
    rating = models.IntegerField(default=0,null =True)
    comment = models.TextField(max_length=2000,default='',null = True)
    author= models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.author} {self.rating} {self.comment} {self.user} {self.time}"


class House(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    category = models.ManyToManyField(Category)
    area = models.FloatField()
    storeys = models.IntegerField()
    repair = models.ManyToManyField(Repair)
    price = models.FloatField()
    currency = models.ManyToManyField(Currency)
    author = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return f"{self.district} {self.street} {self.description}"


class Rooms(models.Model):
    house = models.ManyToManyField(House)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length = 1000,null = True)
    area = models.FloatField()
    image = models.ImageField(upload_to='room_images')

    def __str__(self) -> str:
        return f"{self.house} {self.name} {self.description} {self.area}"


class Payment(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f" {self.house} {self.author} {self.user} {self.price} {self.date} "


class Rental(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_date = models.DateTimeField(auto_now=True)
    to_date = models.DateTimeField(auto_now=True)
    price = models.FloatField()

    def __str__(self) -> str:
        return f" {self.house} {self.author} {self.user} {self.from_date} {self.to_date} {self.price} "


class History(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    payments = models.CharField(max_length=1000)
    rentals = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f" {self.house} {self.payments} {self.rentals} {self.author} {self.date} "

   
