from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum, Count
from .models import Farm, Crop, CropType, IrrigationSchedule, WeatherData
from .forms import CropForm, IrrigationScheduleForm

def home(request):
    """Dashboard showing overview of all farms and crops"""
    if request.user.is_authenticated:
        farms = Farm.objects.filter(owner=request.user)
        total_crops = Crop.objects.filter(farm__owner=request.user).count()
        pending_irrigation = IrrigationSchedule.objects.filter(
            crop__farm__owner=request.user, 
            completed=False,
            scheduled_date__lte=timezone.now()
        ).count()
        
        context = {
            'farms': farms,
            'total_crops': total_crops,
            'pending_irrigation': pending_irrigation,
        }
    else:
        context = {}
    
    return render(request, 'crops/home.html', context)

@login_required
def farm_detail(request, farm_id):
    """Show details of a specific farm"""
    farm = get_object_or_404(Farm, id=farm_id, owner=request.user)
    crops = Crop.objects.filter(farm=farm).select_related('crop_type')
    
    # Calculate farm statistics
    total_area_planted = crops.aggregate(Sum('area_planted'))['area_planted__sum'] or 0
    crops_by_stage = crops.values('current_stage').annotate(count=Count('id'))
    
    context = {
        'farm': farm,
        'crops': crops,
        'total_area_planted': total_area_planted,
        'crops_by_stage': crops_by_stage,
    }
    return render(request, 'crops/farm_detail.html', context)

@login_required
def crop_detail(request, crop_id):
    """Show details of a specific crop"""
    crop = get_object_or_404(Crop, id=crop_id, farm__owner=request.user)
    irrigation_schedule = IrrigationSchedule.objects.filter(crop=crop).order_by('-scheduled_date')
    
    context = {
        'crop': crop,
        'irrigation_schedule': irrigation_schedule,
    }
    return render(request, 'crops/crop_detail.html', context)

@login_required
def add_crop(request, farm_id):
    """Add a new crop to a farm"""
    farm = get_object_or_404(Farm, id=farm_id, owner=request.user)
    
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.farm = farm
            crop.save()
            messages.success(request, f'Successfully added {crop.crop_type.name} to {farm.name}')
            return redirect('farm_detail', farm_id=farm.id)
    else:
        form = CropForm()
    
    context = {
        'form': form,
        'farm': farm,
    }
    return render(request, 'crops/add_crop.html', context)

@login_required
def irrigation_dashboard(request):
    """Show irrigation schedule and management"""
    user_farms = Farm.objects.filter(owner=request.user)
    pending_irrigation = IrrigationSchedule.objects.filter(
        crop__farm__in=user_farms,
        completed=False
    ).select_related('crop', 'crop__farm').order_by('scheduled_date')
    
    completed_today = IrrigationSchedule.objects.filter(
        crop__farm__in=user_farms,
        completed=True,
        completed_date__date=timezone.now().date()
    ).select_related('crop', 'crop__farm')
    
    context = {
        'pending_irrigation': pending_irrigation,
        'completed_today': completed_today,
    }
    return render(request, 'crops/irrigation_dashboard.html', context)

@login_required
def complete_irrigation(request, irrigation_id):
    """Mark an irrigation task as completed"""
    irrigation = get_object_or_404(
        IrrigationSchedule, 
        id=irrigation_id, 
        crop__farm__owner=request.user
    )
    
    irrigation.completed = True
    irrigation.completed_date = timezone.now()
    irrigation.save()
    
    messages.success(request, f'Irrigation completed for {irrigation.crop}')
    return redirect('irrigation_dashboard')

def crop_guide(request):
    """Show crop growing guide and tips"""
    crop_types = CropType.objects.all()
    context = {
        'crop_types': crop_types,
    }
    return render(request, 'crops/crop_guide.html', context)