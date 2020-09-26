from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('entries/<int:pk>/', views.entries, name='entries'),
]