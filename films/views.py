from re import template
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View


from .models import Movie, Actor
from .forms import ReviewForm


class AllMovieView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    paginate_by = 4
    ordering = "-id"

# class MovieView(ListView):
#     model = Movie
#     queryset = Movie.objects.filter(draft=False, category=1)
#     slug_field = 'category'
#     ordering = "-id"


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'



class ActorView(DetailView):
    model = Actor
    template_name = "films/actor.html"




class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
