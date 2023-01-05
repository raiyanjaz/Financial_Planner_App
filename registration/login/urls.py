from django.urls import path 
from .views import Index
from .views import signUp

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('registration/signUp', signUp.as_view(), name='signUp'),
]