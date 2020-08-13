from django.contrib import admin

from .models import Author, Book, Comment, Feedback


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Feedback)