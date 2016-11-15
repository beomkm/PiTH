from django.shortcuts import render
from .models import Log
from django.http import HttpResponse

# Create your views here.
def log_list(request):
	logs = Log.objects.filter().order_by('-time')
	return render(request, 'th/log_list.html', {'logs':logs})



def register(request):
	time = request.GET.get('time')
	temp = request.GET.get('temp')
	humi = request.GET.get('humi')
	Log.objects.create(
			time=time, temp=int(temp), humi=int(humi))
	return HttpResponse("Registerd "+time)

