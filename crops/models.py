from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Farm(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=300)
    total_area = models.DecimalField(max_digits=10, decimal_places=2, help_text="Area in acres")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.owner.username}"

class CropType(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150, blank=True)
    growing_season_days = models.IntegerField(help_text="Average days to harvest")
    water_requirement = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ])
    
    def __str__(self):
        return self.name

class Crop(models.Model):
    GROWTH_STAGES = [
        ('seed', 'Seed/Planting'),
        ('germination', 'Germination'),
        ('vegetative', 'Vegetative Growth'),
        ('flowering', 'Flowering'),
        ('fruiting', 'Fruiting'),
        ('harvest', 'Ready for Harvest'),
        ('harvested', 'Harvested')
    ]
    
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    crop_type = models.ForeignKey(CropType, on_delete=models.CASCADE)
    planted_date = models.DateField()
    area_planted = models.DecimalField(max_digits=8, decimal_places=2, help_text="Area in acres")
    current_stage = models.CharField(max_length=20, choices=GROWTH_STAGES, default='seed')
    expected_harvest_date = models.DateField()
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.crop_type.name} at {self.farm.name}"
    
    @property
    def days_since_planting(self):
        return (timezone.now().date() - self.planted_date).days

class IrrigationSchedule(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()
    duration_minutes = models.IntegerField()
    water_amount_liters = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Irrigation for {self.crop} on {self.scheduled_date.date()}"

class WeatherData(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    date = models.DateField()
    temperature_max = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperature_min = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rainfall = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    class Meta:
        unique_together = ['farm', 'date']
    
    def __str__(self):
        return f"Weather for {self.farm.name} on {self.date}"