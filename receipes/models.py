from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Receipe_name = models.TextField(max_length = 200)
    Receipe_description =  models.TextField(max_length = 300)
    Receipe_image = models.ImageField(upload_to = "Reciepe_Image",max_length=250,default=None)
    