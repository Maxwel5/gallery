from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def home(request):
    return render(request, 'index.html')

def create_album(request):
    images = Image.all_images()
    # return HttpResponse(html)
    return render(request, 'generals/image.html',{"date": date,"news":news})
