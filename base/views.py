from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.


# rooms = [
#     {"id" : 1 , "name": "pyton programming"},
#     {"id" : 2 , "name": "css and html"},
#     {"id" : 3 , "name": "javascript and react"},
# ] 



def home(request):
    rooms = Room.objects.all()
    context = {"rooms" : rooms}
    return render(request, 'home.html', context) 


def room(request, pk):
    room = Room.objects.get(id = pk)
    context = {"room": room} 
    return render(request, 'room.html', context )