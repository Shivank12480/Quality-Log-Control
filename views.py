from django.shortcuts import render
from django.http import JsonResponse
from .models import LogEntry

def index(request):
    return render(request, 'index.html')

def search_logs(request):
    query = request.GET.get('query')
    logs = LogEntry.objects.filter(log_string__icontains=query)
    data = [{'level': log.level, 'log_string': log.log_string, 'timestamp': log.timestamp, 'source': log.source} for log in logs]
    return JsonResponse(data, safe=False)
