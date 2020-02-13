from django.shortcuts import render
from django.conf import settings
from .forms import NumberForm

# Create your views here.
def home(request):
    input=NumberForm()

    return render(request,'home.html',{'input':input})

def result(request):
    if(request.method=='POST'):
        filled_number=NumberForm(request.POST)
        if filled_number.is_valid():
            n1=filled_number.cleaned_data['number1']
            n2=filled_number.cleaned_data['number2']
            renumber=n1+n2


    return render(request,'result.html',{'renumber':renumber})
