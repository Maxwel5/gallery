from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Photo,location

# Create your views here.
# def home(request):
#     return render(request, 'index.html')

def create_album(request):
    photos = Photo.objects.all()
    locations = location.objects.all()
    # return HttpResponse(html)
    return render(request, 'generals/photo.html',{"photos": photos,"locations":locations})

def location(request,location):
    locations = location.objects.all()
    return render(request, 'generals/location.html',{"locations":locations})
