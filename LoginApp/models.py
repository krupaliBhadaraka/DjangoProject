from django.db import models
from django.contrib.auth.models import User
from passlib.hash import pbkdf2_sha256
# Create your models here.


class LoginModel(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def verify_pwd(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
