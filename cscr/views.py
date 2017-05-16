from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,"cscr/index.html")


def introduction(request):
	return render(request,"cscr/introduction.html")

def bulletin(request):
	return render(request,"cscr/bulletin.html")

def people(request):
	return render(request,"cscr/people.html")

def projects(request):
	return render(request,"cscr/projects.html")

def achievements(request):
	return render(request,"cscr/achievements.html")

def publications(request):
	return render(request,"cscr/publications.html")

def database(request):
	return render(request,"cscr/database.html")