from django.urls import path
from . import views
app_name = 'contactos'
urlpatterns = [
    path('', views.contact, name="contactos"),
]