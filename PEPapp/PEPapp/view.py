from django.http import HttpResponse
from ContainerModel.models import Container_list
def list(request):
    response = ''
    list = Container_list.objects.all()
    for var in list:
        response += var.name
    return HttpResponse(response)