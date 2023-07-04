from django.contrib import admin
from .models import Book


class TableAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'id')
    list_display_links = ('title',)


admin.site.register(Book, TableAdmin)
