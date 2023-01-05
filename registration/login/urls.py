from django.urls import path 
from .views import Index
from .views import signUp

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('', signUp.as_view(), name='signUp'),
]