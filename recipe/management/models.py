from django.db import models
from django.contrib.auth.models import User


class ingredients(models.Model):
    name = models.CharField(max_length=90)


class recipe(models.Model):
    recipe_name = models.CharField(max_length=90)
    recipe_descirption = models.TextField()
    ingredient = models.ManyToManyField(ingredients)
    owner = models.ForeignKey(User)


class comments(models.Model):
    user = models.ForeignKey(User)
    comment = models.TextField()


# Create your models here.
