from django.urls import path
from app9_1.views import *
app_name = 'second'

urlpatterns = [
    path('app9_1/',app9_1, name='app9_1')
]