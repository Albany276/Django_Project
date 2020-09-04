from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    # user = models.OneToOneField("user.CustomUser", on_delete=models.CASCADE)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    pass
    def __str__(self):
        return f'{self.user.username} Profile'
    # Decided to include the image as a field in the CustomUser class instead of creating a profile class.

class CustomUser(AbstractUser):
    #this is where I would add custom fields
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    pass

    def __str__(self):
        return self.username