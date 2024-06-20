import csv
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages
from .models import DataFile, DataEntry

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        if file.name.endswith('.json'):
            data = json.load(file)
            data_file = DataFile.objects.create(file=file)
            for entry in data:
                DataEntry.objects.create(data_file=data_file, data=entry, entry_type=entry.get('type', 'unknown'))
            messages.success(request, 'JSON file uploaded successfully.')
        elif file.name.endswith('.csv'):
            data_file = DataFile.objects.create(file=file)
            reader = csv.DictReader(file.read().decode('utf-8').splitlines())
            for entry in reader:
                DataEntry.objects.create(data_file=data_file, data=entry, entry_type=entry.get('type', 'unknown'))
            messages.success(request, 'CSV file uploaded successfully.')
        else:
            messages.error(request, 'Unsupported file type.')
            return redirect('upload')
        return redirect('upload')
    return render(request, 'upload.html')

def query_data(request):
    entry_type = request.GET.get('type')
    if entry_type:
        entries = DataEntry.objects.filter(entry_type=entry_type)
    else:
        entries = DataEntry.objects.all()
    return render(request, 'data_table.html', {'entries': entries})
