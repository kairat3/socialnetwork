from django.urls import path, include
from . import views


urlpatterns = [
    path('posts/create/', views.PostCreateView.as_view()),
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view())
]
