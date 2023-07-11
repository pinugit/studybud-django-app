from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


rooms = [
    {"id" : 1 , "name": "pyton programming"},
    {"id" : 2 , "name": "css and html"},
    {"id" : 3 , "name": "javascript and react"},
] 



def home(request):
    return render(request, 'home.html' ,{"rooms" : rooms})


def room(request, pk):
    return render(request, 'room.html')