from django.urls import path

from .views import homePageView, createView, deleteEvent, registerView

urlpatterns = [
    path('', homePageView, name='home'),
    path('create/',  createView, name='create'),
    path('delete/<int:event_id>/', deleteEvent, name='delete'),
    path('register/', registerView, name='register'),
]