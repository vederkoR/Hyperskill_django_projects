from django.db import models

class Frame(models.Model):
    color = models.CharField(max_length=128)
    quantity = models.IntegerField()


class Seat(models.Model):
    color = models.CharField(max_length=128)
    quantity = models.IntegerField()


class Tire(models.Model):
    type = models.CharField(max_length=128)
    quantity = models.IntegerField()


class Basket(models.Model):
    quantity = models.IntegerField()


class Bike(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    has_basket = models.BooleanField()
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)


class Order(models.Model):
    P = "pending"
    R = "ready"
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    status = models.CharField(max_length=128, choices=[(P, "pending"), (R, "ready")])
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
