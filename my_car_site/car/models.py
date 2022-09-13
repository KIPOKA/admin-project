from django.db import models

# Create your models here.
class Car(models.Model):
    year = models.CharField(max_length=30)
    brand = models.IntegerField()

    def __str__(self):
        return f"Car is {self.brand} {self.year}"
