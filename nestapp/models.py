from tabnanny import verbose
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    """
    List of all Counties involved
    """
    KISUMU = 'KSM'
    NAIROBI = 'NRB'
    MOMBASA = 'MSA'
    
    COUNTIES = [
        (KISUMU, 'Kisumu'),
        (NAIROBI, 'Nairobi'),
        (MOMBASA, 'Mombasa')
    ]
    
    county = models.CharField(
        max_length=3,
        choices=COUNTIES, 
        default=NAIROBI)
    
    description = models.TextField()
    created_by = models.CharField(max_length=50, null=False, blank=True)
    date_created = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "location_point"
        
    def __str__(self):
        return self.name
        
        
        
        
class Trip(models.Model):
    name = models.CharField(max_length=50, null=False, blank=True)
    trip_from = models.ForeignKey(Location, default=1, related_name="trip_start", on_delete=models.CASCADE)
    trip_to = models.ForeignKey(Location, default=2, related_name="trip_end", on_delete=models.CASCADE)
    receiver_id = models.CharField(max_length=50, null=False, blank=True)
    created_by = models.CharField(max_length=50, null=False, blank=True)
    date_created = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    class Meta:
        ordering = ['-date_created']
        
        
    def __str__(self):
        return self.name


class TripLocation(models.Model):
    trip_id= models.ForeignKey(Trip, null=False, blank=False, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, null=False, blank=False, on_delete=models.CASCADE)
    
    
