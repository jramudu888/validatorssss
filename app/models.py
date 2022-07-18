from django.db import models

# Create your models here.
class validating(models.Model):
    Vid=models.PositiveIntegerField(primary_key=True)
    Vname=models.CharField(max_length=100)

    def __str__(self):
        return self.Sname