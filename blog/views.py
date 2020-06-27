from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
	{
	"Title": "Hello World",
	"Auther": "User1",
	"Content": "Lorem text goes here for testing"
	},
	{
	"Title": "New Morning",
	"Auther": "User2",
	"Content": "A New morning Lorem text goes here for testing"
	},

	]
	

def home(request):
	context = {
		"posts":posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	# return HttpResponse('<h1 /> Blog About')
	return render(request, 'blog/about.html', {'title': 'about'})