from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_all_persons_page, name='show_all_persons_page'),
]