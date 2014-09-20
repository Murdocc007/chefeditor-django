import hashlib
from django.db import models
from django import forms



class Login(models.Model):
    email = models.EmailField(max_length = 255, unique=True)
    password = models.CharField(max_length = 255, default = None, null=True)

    def __unicode__(self):
        return self.email

    def create_hash(self):
        m = hashlib.md5()
        m.update(self.password)
        return m.hexdigest()

    def save(self, *args, **kwargs):
        if self.password is not None:
            self.password = self.create_hash()
        super(Login, self).save(*args, **kwargs)



class Users(models.Model):
    login = models.ForeignKey('Login')
    name = models.CharField(max_length = 255)
    profile_pic = models.CharField(max_length = 255)



class ProfilePic(models.Model):
    login=models.ForeignKey('Login',null=True)
    profpic = models.FileField(upload_to="images/")

class ProfilePicForm(forms.Form):
    profpic = forms.FileField(
        label='Select an image file',
        )
    
class Fiddle(models.Model):
    login = models.ForeignKey('Login')
    name=models.CharField(max_length = 255)
    html=models.CharField(max_length = 255)
    javascript=models.CharField(max_length = 255)
    css=models.CharField(max_length = 255)
    public_temp=models.DecimalField(max_digits = 3,decimal_places=2,default=0)
    
