from django.http import HttpResponse
from django.template import loader

def members(request):
  temp = loader.get_temp('LOL.html')
  return HttpResponse(temp.render())