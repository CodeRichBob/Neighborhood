from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    neighbourhood = models.ForeignKey('neighbourhoodapp.Neighbourhood', on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'