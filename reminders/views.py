from django.shortcuts import render

# Create your views here.
# Assuming you have Django installed and a Django project set up

# First, create a Django app (if not already created)
# Run the following command in your terminal:
# python manage.py startapp reminders

# Then, in your Django app's views.py file, create the API endpoint

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reminder
import json

@csrf_exempt
def create_reminder(request):
    if request.method == 'POST':
        # Assuming the request body contains JSON data
        data = json.loads(request.body)

        # Extracting data from the JSON request
        date = data.get('date')
        time = data.get('time')
        message = data.get('message')

        # Saving the reminder to the database
        reminder = Reminder.objects.create(date=date, time=time, message=message)
        reminder.save()

        return JsonResponse({'success': True, 'message': 'Reminder created successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
