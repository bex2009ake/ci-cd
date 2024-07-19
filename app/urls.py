from django.urls import path
from app.views import *

urlpatterns = [
    path('res/', resp, name='resp'),
    path('res2/', resp2, name='resp2'),
    path('res3/', resp3, name='resp3'),
]
