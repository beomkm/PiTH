from django.shortcuts import render
from .models import Log
from django.http import HttpResponse

# Create your views here.
def log_list(request):
	logs = Log.objects.filter().order_by('-time')[:10]
	logs_graph = reversed(logs)
	return render(request, 'th/log_list.html', {'logs':logs, 'logs_graph':logs_graph})


def register(request):
	time = request.GET.get('time')
	temp = request.GET.get('temp')
	humi = request.GET.get('humi')
	Log.objects.create(
			time=time, temp=int(temp), humi=int(humi))
	return HttpResponse("Registered "+time)


def clear(request):
	Log.objects.all().delete()
	return HttpResponse("All data was deleted.")
