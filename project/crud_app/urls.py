from django.urls import path
from .views import add_movieticket,show_movieticket,update_movieticket,cancel_movieticket

urlpatterns = [
    path('add/',add_movieticket, name='add_url'),
    path('show/',show_movieticket, name='show_url'),
    path('update/<int:pk>/',update_movieticket, name='update_url'),
    path('cancel/<int:pk>/',cancel_movieticket, name='cancel_url'),
]