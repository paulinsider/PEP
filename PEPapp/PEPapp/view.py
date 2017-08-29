from django.http import HttpResponse,JsonResponse
from ContainerModel.models import Container_list
from django.shortcuts import render
import os
def index(request):
    return render(request, 'common/index.html')

def list(request):
    response = []
    list = Container_list.objects.all()
    for var in list:
        if var.show_type != 1:
            response.append(var)
    return render(request, 'common/list.html', {'data':response})

'''
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
'''


def manageApp(request):
    action = request.POST['action']
    id = int(request.POST['id'])
    list = Container_list.objects.all()
    response = dict()
    for var in list:
        if var.show_type == 1 and var.id == id:
            return HttpResponse(
                JsonResponse({"status": "failed", "comment": "该镜像已经被删除！"}, content_type="application/json"))
        if var.show_type == 1 :
            continue
        if var.status == 1 and action == 'start' and var.id != id:
            return HttpResponse(JsonResponse({"status":"failed","comment":"用户一次只能申请一个练习环境。"}, content_type="application/json"))
        if var.id == id:
            if action == 'start' and var.status == 0:
                path = "sh /home/PEP.sh " + var.path + " start"
                os.system(path)
                var.status = 1
                var.save()
            elif action == 'stop' and var.status == 1:
                path = "sh /home/PEP.sh " + var.path + " stop"
                os.system(path)
                var.status=0
                var.save()
            return HttpResponse(JsonResponse({"status":"success"}, content_type="application/json"))
    return HttpResponse(JsonResponse({"status":"failed","comment":"失败请重试！"}, content_type="application/json"))