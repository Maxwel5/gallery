from django.shortcuts import render
from django.http  import HttpResponse,Http404
# from .models import Image

# Create your views here.
def home(request):
    return render(request, 'index.html')

def create_album(request):
    images = Image.all_images()
    locations = Location.objects.all()
    # return HttpResponse(html)
    return render(request, 'generals/image.html',{"images": images,"locations":locations})

def location(request,location):
    locations = Location.objects.all()
    return render(request, 'generals/location.html',{"locations":locations})
