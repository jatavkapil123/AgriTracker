# AgriTracker - Smart Farm Management System

AgriTracker is a Django-based web application designed to help farmers manage their crops, track growth stages, and optimize irrigation schedules. This application addresses real-world agriculture challenges by providing a centralized platform for farm management.

## Features

### 🌱 Crop Management
- Track multiple crops across different farms
- Monitor growth stages from planting to harvest
- Record planting dates and expected harvest times
- Maintain detailed notes for each crop

### 💧 Irrigation Management
- Schedule irrigation tasks for different crops
- Track water usage and irrigation duration
- Mark irrigation tasks as completed
- Dashboard view for pending and completed irrigation

### 🚜 Farm Organization
- Manage multiple farms per user
- Track farm locations and total area
- Monitor area utilization across crops
- Farm-specific crop statistics

### 📊 Analytics & Insights
- Days since planting calculations
- Crop distribution by growth stages
- Irrigation scheduling and completion tracking
- Farm utilization statistics

### 📚 Crop Guide
- Information about different crop types
- Growing season duration and water requirements
- Seasonal planting calendar
- Best practices for planting, watering, and pest management

## Real-World Problems Solved

1. **Crop Tracking**: Farmers often struggle to keep track of multiple crops planted at different times. AgriTracker provides a centralized system to monitor all crops and their growth stages.

2. **Irrigation Management**: Proper irrigation scheduling is crucial for crop success. The application helps farmers schedule, track, and optimize their irrigation practices.

3. **Farm Organization**: Managing multiple plots or farms can be complex. AgriTracker organizes farm data and provides clear visibility into farm utilization.

4. **Knowledge Management**: New farmers or those trying new crops benefit from the integrated crop guide with best practices and seasonal information.

## Technology Stack

- **Backend**: Django 6.0.1
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: Bootstrap 5.1.3 with responsive design
- **Icons**: Font Awesome 6.0.0
- **Authentication**: Django's built-in user system

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Quick Start

1. **Clone and setup the project:**
   ```bash
   # Navigate to your project directory
   cd your-project-directory
   
   # Create virtual environment
   python3 -m venv agri_env
   source agri_env/bin/activate  # On Windows: agri_env\Scripts\activate
   
   # Install Django
   pip install django
   ```

2. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create sample data:**
   ```bash
   python manage.py populate_sample_data
   ```

4. **Create admin user (optional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

### Sample Login Credentials

After running `populate_sample_data`, you can login with:
- **Username**: farmer
- **Password**: farming123

Admin credentials (if created):
- **Username**: admin
- **Password**: admin123

## Usage Guide

### For Farmers

1. **Dashboard**: View overview of all farms, crops, and pending irrigation tasks
2. **Farm Management**: Click on any farm to see detailed crop information
3. **Add Crops**: Use the "Add Crop" button to plant new crops
4. **Irrigation**: Use the irrigation dashboard to manage watering schedules
5. **Crop Guide**: Reference the crop guide for growing tips and best practices

### For Administrators

1. **Admin Panel**: Access via `/admin/` to manage users, farms, and crop types
2. **User Management**: Create farmer accounts and assign farms
3. **Crop Types**: Add new crop varieties with their characteristics
4. **Data Management**: View and manage all system data

## Models Overview

- **Farm**: Represents a farm with location and area information
- **CropType**: Defines crop varieties with growing characteristics
- **Crop**: Individual crop plantings with growth tracking
- **IrrigationSchedule**: Irrigation tasks and completion tracking
- **WeatherData**: Weather information for farms (extensible)

## Future Enhancements

- Weather API integration for automatic weather data
- Mobile app for field data collection
- Pest and disease tracking
- Harvest yield recording and analytics
- Market price integration
- Automated irrigation recommendations
- Photo documentation for crop progress
- Export functionality for reports

## Contributing

This is a basic implementation that can be extended based on specific farming needs. Key areas for enhancement:

1. **Weather Integration**: Connect to weather APIs for automatic data collection
2. **Mobile Optimization**: Enhance mobile experience for field use
3. **Reporting**: Add comprehensive reporting and analytics
4. **Notifications**: Email/SMS alerts for irrigation and harvest times
5. **Multi-language**: Support for local languages

## License

This project is created for educational and practical farming purposes. Feel free to modify and adapt it to your specific agricultural needs.

## Support

For questions or support, please refer to the Django documentation or create an issue in the project repository.

---

**AgriTracker** - Helping farmers grow smarter! 🌱