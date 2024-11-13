from django.shortcuts import render
from .models import Category
# Create your views here.


def what_in_db(request):
    categories = Category.objects.values('id','name','max_occupants')
    context = {'categories':categories}
    return render(request, 'hotel/index.html',context)
