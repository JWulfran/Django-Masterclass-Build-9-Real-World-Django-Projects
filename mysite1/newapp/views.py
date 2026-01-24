from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.
def movie_list(request):
    movie_objects = Movies.objects.all()

    paginator = Paginator(movie_objects, 4)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)

    return render(request, 'newapp/movie_list.html', {'movie_objects': movie_objects})
