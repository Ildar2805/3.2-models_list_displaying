from django.contrib import admin

from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'pub_date', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Book, BookAdmin)
