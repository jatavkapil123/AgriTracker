from django.contrib import admin
from .models import Farm, CropType, Crop, IrrigationSchedule, WeatherData

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'location', 'total_area', 'created_at']
    list_filter = ['created_at', 'owner']
    search_fields = ['name', 'location', 'owner__username']

@admin.register(CropType)
class CropTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'scientific_name', 'growing_season_days', 'water_requirement']
    list_filter = ['water_requirement']
    search_fields = ['name', 'scientific_name']

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ['crop_type', 'farm', 'planted_date', 'current_stage', 'area_planted', 'expected_harvest_date']
    list_filter = ['current_stage', 'planted_date', 'crop_type', 'farm']
    search_fields = ['crop_type__name', 'farm__name']
    date_hierarchy = 'planted_date'

@admin.register(IrrigationSchedule)
class IrrigationScheduleAdmin(admin.ModelAdmin):
    list_display = ['crop', 'scheduled_date', 'duration_minutes', 'completed', 'completed_date']
    list_filter = ['completed', 'scheduled_date', 'crop__farm']
    search_fields = ['crop__crop_type__name', 'crop__farm__name']
    date_hierarchy = 'scheduled_date'

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['farm', 'date', 'temperature_max', 'temperature_min', 'humidity', 'rainfall']
    list_filter = ['date', 'farm']
    search_fields = ['farm__name']
    date_hierarchy = 'date'