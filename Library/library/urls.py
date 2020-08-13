from django.urls import path

from .views import main, books, authors, feedback, certain_book, certain_author

app_name = 'library'
urlpatterns = [
    path('', main, name='main'),
    path('books/', books, name='books'),
    path('books/<int:book_id>', certain_book, name='certain_book'),
    path('authors/', authors, name='authors'),
    path('authors/<int:author_id>', certain_author, name='certain_author'),
    path('feedback/', feedback, name='feedback'),
]
