from django.urls import path
# import views so we can register our class-based views in path below
from . import views

urlpatterns = [
    # add new path with music/ as the endpoint
    # register our model class list class based view as a view (query)
    path('music/', views.SongList.as_view()),
]