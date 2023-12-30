from django.urls import path

from .views import homePageView, createView

urlpatterns = [
    path('', homePageView, name='home'),
    path('create/',  createView, name='create')
]