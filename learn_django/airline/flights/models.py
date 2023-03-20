from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    #on_delete=models.CASCADE is a parameter in Django's model fields
    #that specifies what should happen when the referenced object is deleted.
    #when the referenced object is deleted, all related objects that 
    # depend on it will also be deleted. 
    #related_name is a parameter that is used to specify the name of the reverse relation 
    #from the related model back to the model that defines the ForeignKey.
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"