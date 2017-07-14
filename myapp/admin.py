from django.contrib import admin
from .models import TodoBord


class TodoBordAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'new_message')

admin.site.register(TodoBord, TodoBordAdmin)
