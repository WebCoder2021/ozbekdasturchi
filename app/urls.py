from django.urls import path
from .views import *

urlpatterns = [
    path('base/', base  , name='base'),
    path('', home  , name='home'),
    path('category/<slug:slug>/', category ),
    path('blog/<int:pk>/', single ),
    # path('', home  , name='home'),
]