from django.db import models
from distutils.command.upload import upload

class registration(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    id_proof = models.ImageField(null=True, upload_to='photo/')
    photo = models.ImageField(null=True, upload_to='id/')

# Create your models here.
class login(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    user_id = models.IntegerField()
