from django.shortcuts import render
from django.http import HttpResponse
from base.models import Room,Image,Video

def home(request):
    room=Room.objects.all()
    contxt={'room':room}
    return render(request,'base/home.html',contxt)

def room(request,pk):
    rooms=Room.objects.get(id=pk)
    return render(request,'base/room.html')

def image(request):
     img=Image.objects.all()
     contxr={'img':img}
     return render(request,'base/image.html',contxr)

def index(request):
    video=Video.objects.all()

    return render(request,'base/index.html',{'video':video})


 

