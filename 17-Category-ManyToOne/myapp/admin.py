from django.contrib import admin
from myapp.models import Flower, Category # < here
admin.site.register(Flower)
admin.site.register(Category) # < here