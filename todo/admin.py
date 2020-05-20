from django.contrib import admin
from .models import Todo

# Allows you to read a field that is not allowed to be edited
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)