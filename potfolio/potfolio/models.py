from django.db import models

class About(models.Model):
    u_name = models.CharField(max_length=500)
    dob = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500, unique=True)
    no_exp = models.CharField(max_length=5000)
    no_happy_customers = models.CharField(max_length=500)
    no_project_finished = models.CharField(max_length=500)
    no_digital_awards = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    date_time = models.CharField(max_length=500)
    v_c = models.CharField(max_length=500)
    v_status = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

class companins(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")