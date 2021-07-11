from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'language', 'total_copies', 'available_copies', 'pic']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll_no', 'email', 'contact_no', 'course', 'total_books_Due', 'pic', 'user']

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'issue_date', 'return_date']

