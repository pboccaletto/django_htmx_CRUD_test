from django.db import models

# Create your models here.
class UserProfile(models.Model):
    """
    Model to store user profile information
    """
    name = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surename}"