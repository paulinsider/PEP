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
    return HttpResponse(response)

def startapp(request):
    id = request.GET['id']
    whereparam = "id=" + id
    object = Container_list.objects.get(whereparam)
    path = "./" + object.path + " start"
    os.system(path)
    object.status = 1
    object.save()
    return HttpResponse("112.74.63.70:9001")

def stopapp(request):
    id = request.GET['id']
    whereparam = "id=" + id
    object = Container_list.objects.get(whereparam)
    path = "./" + object.path + " start"
    os.system(path)
    object.status = 0
    object.save()
    return HttpResponse("container has stopped")