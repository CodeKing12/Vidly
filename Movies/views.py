from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, template_name="Movies/index.html", context={"movies": movies})

def details(request, movies_id):
    movie = get_object_or_404(Movie, id=movies_id)
    return render(request, "Movies/details.html", {"movie": movie})
