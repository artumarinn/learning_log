from django.contrib import admin
from .models import Topic, Entry

admin.site.register(Topic) #  Gestionar modelo a traves de un sitio admin
admin.site.register(Entry)