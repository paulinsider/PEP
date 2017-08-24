from django.http import HttpResponse
from ContainerModel.models import Container_list
from django.shortcuts import render
import os
def index(request):
    return render(request, 'common/index.html')

def list(request):
    response = []
    list = Container_list.objects.all()
    for var in list:
        response.append(var)
    return render(request, 'common/list.html', {'data':response})

def startapp(request):
    id = request.GET['id']
    whereparam = {'id':id}
    object = Container_list.objects.get(**whereparam)
    if object.status == 0:
        path = "sh /home/PEP.sh " + object.path + " start"
        os.system(path)
        object.status = 1
        object.save()
    response = []
    list = Container_list.objects.all()
    for var in list:
        response.append(var)
    return render(request, 'common/list.html', {'data': response})

def stopapp(request):
    id = request.GET['id']
    whereparam = {'id': id}
    object = Container_list.objects.get(**whereparam)
    if object.status == 1:
        path =  "sh /home/PEP.sh " + object.path + " stop"
        os.system(path)
        object.status = 0
        object.save()
    response = []
    list = Container_list.objects.all()
    for var in list:
        response.append(var)
    return render(request, 'common/list.html', {'data': response})
