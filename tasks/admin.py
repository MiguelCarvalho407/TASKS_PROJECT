from django.contrib import admin
from .models import Utilizadores, Task, Category

admin.site.register(Utilizadores)
admin.site.register(Category)
admin.site.register(Task)