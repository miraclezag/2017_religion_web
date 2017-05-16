from django.conf.urls import url
from . import views

urlpatterns=[
	url(r"^$",views.index, name="index"),
	url(r"^introduction",views.introduction,name="introduction"),
	url(r"^bulletin",views.bulletin,name="bulletin"),
	url(r"^people",views.people,name="people"),
	url(r"^projects",views.projects,name="projects"),
	url(r"^publications",views.publications,name="publications"),
	url(r"^achievements",views.achievements,name="achievements"),
	url(r"^database",views.database,name="database"),
]