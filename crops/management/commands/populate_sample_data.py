from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from crops.models import Farm, CropType, Crop, IrrigationSchedule

class Command(BaseCommand):
    help = 'Populate database with sample agriculture data'

    def handle(self, *args, **options):
        # Create sample crop types
        crop_types_data = [
            {'name': 'Tomato', 'scientific_name': 'Solanum lycopersicum', 'growing_season_days': 80, 'water_requirement': 'high'},
            {'name': 'Wheat', 'scientific_name': 'Triticum aestivum', 'growing_season_days': 120, 'water_requirement': 'medium'},
            {'name': 'Corn', 'scientific_name': 'Zea mays', 'growing_season_days': 100, 'water_requirement': 'medium'},
            {'name': 'Rice', 'scientific_name': 'Oryza sativa', 'growing_season_days': 150, 'water_requirement': 'high'},
            {'name': 'Potato', 'scientific_name': 'Solanum tuberosum', 'growing_season_days': 90, 'water_requirement': 'medium'},
            {'name': 'Carrot', 'scientific_name': 'Daucus carota', 'growing_season_days': 70, 'water_requirement': 'low'},
        ]

        for crop_data in crop_types_data:
            crop_type, created = CropType.objects.get_or_create(
                name=crop_data['name'],
                defaults=crop_data
            )
            if created:
                self.stdout.write(f'Created crop type: {crop_type.name}')

        # Create a sample user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='farmer',
            defaults={
                'email': 'farmer@example.com',
                'first_name': 'John',
                'last_name': 'Farmer'
            }
        )
        if created:
            user.set_password('farming123')
            user.save()
            self.stdout.write('Created sample user: farmer (password: farming123)')

        # Create sample farms
        farms_data = [
            {'name': 'Green Valley Farm', 'location': 'California, USA', 'total_area': 50.0},
            {'name': 'Sunrise Agriculture', 'location': 'Texas, USA', 'total_area': 75.5},
        ]

        for farm_data in farms_data:
            farm, created = Farm.objects.get_or_create(
                name=farm_data['name'],
                owner=user,
                defaults=farm_data
            )
            if created:
                self.stdout.write(f'Created farm: {farm.name}')

        # Create sample crops
        farms = Farm.objects.filter(owner=user)
        if farms.exists():
            farm = farms.first()
            
            # Get some crop types
            tomato = CropType.objects.get(name='Tomato')
            wheat = CropType.objects.get(name='Wheat')
            corn = CropType.objects.get(name='Corn')

            crops_data = [
                {
                    'crop_type': tomato,
                    'planted_date': timezone.now().date() - timedelta(days=30),
                    'area_planted': 5.0,
                    'current_stage': 'vegetative',
                    'expected_harvest_date': timezone.now().date() + timedelta(days=50),
                    'notes': 'Growing well, regular watering needed'
                },
                {
                    'crop_type': wheat,
                    'planted_date': timezone.now().date() - timedelta(days=60),
                    'area_planted': 15.0,
                    'current_stage': 'flowering',
                    'expected_harvest_date': timezone.now().date() + timedelta(days=60),
                    'notes': 'Good growth, monitor for pests'
                },
                {
                    'crop_type': corn,
                    'planted_date': timezone.now().date() - timedelta(days=45),
                    'area_planted': 10.0,
                    'current_stage': 'vegetative',
                    'expected_harvest_date': timezone.now().date() + timedelta(days=55),
                    'notes': 'Healthy plants, increase watering frequency'
                }
            ]

            for crop_data in crops_data:
                crop, created = Crop.objects.get_or_create(
                    farm=farm,
                    crop_type=crop_data['crop_type'],
                    planted_date=crop_data['planted_date'],
                    defaults=crop_data
                )
                if created:
                    self.stdout.write(f'Created crop: {crop.crop_type.name} at {crop.farm.name}')

                    # Create sample irrigation schedules
                    for i in range(3):
                        irrigation_date = timezone.now() + timedelta(days=i+1, hours=6)
                        irrigation, created = IrrigationSchedule.objects.get_or_create(
                            crop=crop,
                            scheduled_date=irrigation_date,
                            defaults={
                                'duration_minutes': 30,
                                'water_amount_liters': 100.0,
                                'notes': f'Regular irrigation schedule for {crop.crop_type.name}'
                            }
                        )
                        if created:
                            self.stdout.write(f'Created irrigation schedule for {crop.crop_type.name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated sample agriculture data!')
        )
        self.stdout.write('You can now login with username: farmer, password: farming123')