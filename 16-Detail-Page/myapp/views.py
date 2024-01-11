from django.shortcuts import render, get_object_or_404 # < \here
from .models import Flower
def index(request):
    flowers = Flower.objects.all()
    return render(request, 'myapp/index.html', {'flowers': flowers})
def detail(request, id=None): # < here
    flower = get_object_or_404(Flower, slug=slug) # < here
    return render(request, 'myapp/detail.html', {'flower': flower})