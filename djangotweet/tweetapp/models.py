from django.db import models
from django.forms import ModelForm
# Create your models here.

class Tweet(models.Model):
    nickname = models.CharField(max_length=50)
    message = models.CharField(max_length=100)


    def __str__(self) -> str:
        return f"Nickname: {self.nickname}, Message: {self.message}"
    

