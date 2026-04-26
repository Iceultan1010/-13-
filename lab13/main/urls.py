from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('notes/create/', views.note_create_view, name='note_create'),
    path('notes/<int:pk>/edit/', views.note_edit_view, name='note_edit'),
    path('notes/<int:pk>/delete/', views.note_delete_view, name='note_delete'),
]
