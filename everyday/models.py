from django.db import models


# Create your models here.

class Expenses(models.Model):
    date = models.IntegerField()
    food = models.IntegerField()
    cafe = models.IntegerField()
    cloth = models.IntegerField
    other = models.IntegerField()
    communal = models.IntegerField()
    month_finish = models.BooleanField(default=False)
    objects = models.Manager()


