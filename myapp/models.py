from django.db import models

# Create your models here.

MALE = 'Male'
FEMALE = 'Female'

GENDER_CHOICES = [
    (MALE, MALE),
    (FEMALE, FEMALE),
]

class Person(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    age = models.IntegerField(default=5)