from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.IntegerField
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
