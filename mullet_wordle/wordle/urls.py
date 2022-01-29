from django.urls import path
from wordle import views

app_name = 'wordle'

urlpatterns = [
    path('', views.wordle, name='wordle'),
]