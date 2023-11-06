from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class register_model(User):
    phone = models.PositiveBigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[
                              ['Male', 'Male'], ['Female', 'Female']])
    img = models.ImageField(upload_to='profile_pics/')
