from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Crop, CropType, IrrigationSchedule

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['crop_type', 'planted_date', 'area_planted', 'expected_harvest_date', 'notes']
        widgets = {
            'planted_date': forms.DateInput(attrs={'type': 'date'}),
            'expected_harvest_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['crop_type'].queryset = CropType.objects.all()
        
        # Set default dates
        if not self.instance.pk:
            self.fields['planted_date'].initial = timezone.now().date()
            self.fields['expected_harvest_date'].initial = timezone.now().date() + timedelta(days=90)

class IrrigationScheduleForm(forms.ModelForm):
    class Meta:
        model = IrrigationSchedule
        fields = ['scheduled_date', 'duration_minutes', 'water_amount_liters', 'notes']
        widgets = {
            'scheduled_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default scheduled date to tomorrow morning
        if not self.instance.pk:
            tomorrow = timezone.now() + timedelta(days=1)
            self.fields['scheduled_date'].initial = tomorrow.replace(hour=6, minute=0, second=0, microsecond=0)