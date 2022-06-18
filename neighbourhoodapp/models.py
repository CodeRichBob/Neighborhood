from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hood')
    neighbourhood_logo = CloudinaryField('image')
    description = models.TextField()
    health_number = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)
    occupant_count = models.IntegerField(null=True, blank=True)