from django.shortcuts import render
import datetime
# Create your views here.

def filters(request):
    dt=datetime.datetime.now()
    d={'data':'thiS iS buILt IN filTERs','dt':dt,'c':5}

    return render(request,'filters.html',d)


def user(request):

    d={'value':'today WE are LearNiNg ABOut UsErDEfined FILTERs'}
    
    return render(request,'user.html',d)