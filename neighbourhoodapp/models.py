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

    def __str__(self):
        return f'{self.name}hood'

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()
    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        return cls.objects.filter(id=neighbourhood_id)