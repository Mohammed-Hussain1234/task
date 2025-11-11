from django.urls import path
from .views import *

urlpatterns=[
    path('home/',about_view),
    path('house/',lak),
    path('shop/<name>',home),
    path('square/<int:number>/',hrs),
]

