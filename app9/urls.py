from django.urls import path
from app9.views import *
app_name='app9'

urlpatterns = [
    path('app9/', app9, name='app9'),
]
