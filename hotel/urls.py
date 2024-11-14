from django.urls import path
from . import views


urlpatterns = [
    path('', views.categories, name='categories'),
    path('categories/<int:category_id>/<str:category_name>/', views.category, name='category')
]
