from django.shortcuts import render
from .models import Do
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Do


# Create your views here.
def home(request):
    do_list=Do.objects.all().order_by("-date")
    current_time=timezone.now()
    return render(request,'home.html',{'do_list':do_list,'timezone':current_time})

@csrf_exempt
def add_task(request):
    current_time=timezone.now()
    content=request.POST['content']
    Do.objects.create(date=current_time,task=content)
    return HttpResponseRedirect("/")
@csrf_exempt
def delete_task(request,id):
    Do.objects.get(id=id).delete()

    return HttpResponseRedirect("/")
@csrf_exempt
def edit_task(request,id):
    presentobj=Do.objects.get(id=id)
    newtask=request.POST['newtask']
    time=presentobj.date
    Do.objects.get(id=id).delete()
    Do.objects.create(date=time,task=newtask)
    return HttpResponseRedirect("/")
@csrf_exempt
def search(request):
    list_of_object=Do.objects.all()
    given=request.POST['given']
    return render(request,'search.html',{'list_of_object':list_of_object,'given':given})
