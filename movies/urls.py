from django.urls import path
# import views
from movies import views
urlpatterns = [
    path("movies/",views.Movies.as_view())
]