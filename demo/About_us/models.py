from django.db import models

# Create your models here.
class Teachers(models.Model):
    T_Name = models.CharField(max_length=40)
    T_Email = models.CharField(max_length=30)