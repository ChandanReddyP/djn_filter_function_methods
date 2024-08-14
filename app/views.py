from django.shortcuts import render
import datetime
# Create your views here.

def filters(request):
    dt=datetime.datetime.now()
    d={'data':'thiS iS buILt IN filTERs','dt':dt,'c':5}

    return render(request,'filters.html',d)