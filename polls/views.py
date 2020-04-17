from django.shortcuts import render

from django.http import HttpResponse
from .models import Choice


def index(request):
   #  return HttpResponse("Hello, world. You're at the polls index.")
   latest_choice_list = Choice.objects.all()
   context = {'latest_choice_list': latest_choice_list}
   return render(request, 'polls/index.html', context)
# Create your views here.
