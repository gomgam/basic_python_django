from django.db import models

# Create your models here.


class Competitor(models.Model):
    name = models.TextField()
    nickname = models.TextField()
    no = models.IntegerField(unique=True)