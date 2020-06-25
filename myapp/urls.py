from django.urls import path

from . import views

handler404 = views.handler404

urlpatterns = [
    path('', views.show_all_persons_page, name='show_all_persons_page'),
]