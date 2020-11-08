from django.db import models


# Create your models here.
class Position(models.Model):
    x_position = models.IntegerField(default=0)
    y_position = models.IntegerField(default=0)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self
