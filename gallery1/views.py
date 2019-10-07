from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Photo,location

# Create your views here.
# def home(request):
#     return render(request, 'index.html')

def create_album(request):
    photos = Photo.objects.all()
    print(photos)
    return render(request, 'generals/photo.html',{"photos": photos})

def location(request,location):
    locations = location.objects.all()
    selected_location = location.objects.get(id = location)
    images = Image.objects.filter(location = selected_location.id)

    return render(request, 'generals/location.html',{"locations":locations,"location":selected_location,"images":images})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'generals/search.html',{"photos":searched_photos,"message":message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'generals/search.html',{"photos":searched_photos})