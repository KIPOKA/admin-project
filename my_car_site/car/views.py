from django.shortcuts import render

from . import models
# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars':all_cars}
    return render(request,'car/list.html', context=context)
def delete(request):
    return render(request,'car/delete.html')
def add(request):
    return render(request,'car/add.html')