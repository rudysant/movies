from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib import messages

# Create your views here.

def addmovie(request):
	if request.method == "POST":
		movie_form = MovieForm(request.POST, request.FILES)
		if movie_form.is_valid():
			movie_form.save()
			messages.success(request, ('Your movie was successfully added!'))
		else:
			messages.error(request, 'Error saving form')
		
		
		return redirect("listmovie")
	movie_form = MovieForm()
	movies = Movie.objects.all()
	return render(request=request, template_name="home.html", context={'movie_form':movie_form})

def listmovie(request):
	movies = Movie.objects.all()
	return render(request=request, template_name="listmovie.html", context={'movies':movies})
# Create your views here.
