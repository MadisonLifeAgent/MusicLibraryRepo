from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:pk>/', views.SongDetail.as_view()),
    path('music/<int:pk>/edit/', views.SongDetail.as_view()),
    path('music/<int:pk>/delete/', views.SongDetail.as_view()),
    path('music/<int:pk>/likes/', views.Likes.as_view()),
]