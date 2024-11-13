from django.urls import path
from . import views


urlpatterns = [
    path('',views.what_in_db,name='trial')
]
