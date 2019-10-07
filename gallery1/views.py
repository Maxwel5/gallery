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

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_photos = category.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'generals/search.html',{"photos":searched_photos,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'generals/search.html',{"photos":searched_photos})