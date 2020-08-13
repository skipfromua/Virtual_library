from django.shortcuts import render

from .services import get_user_and_form_context, get_user_books_and_form_context_with_filter, \
    get_user_book_and_form_context, get_user_authors_and_form_context, get_user_author_and_form_context, \
    get_user_and_send_feedback


def main(request):
    return render(request, 'library/index.html', get_user_and_form_context(request))


def books(request):
    return render(request, 'library/books.html', get_user_books_and_form_context_with_filter(request))


def certain_book(request, book_id):
    return render(request, 'library/detail_book.html', get_user_book_and_form_context(request, book_id))


def authors(request):
    return render(request, 'library/authors.html', get_user_authors_and_form_context(request))


def certain_author(request, author_id):
    return render(request, 'library/detail_author.html', get_user_author_and_form_context(request, author_id))


def feedback(request):
    return render(request, 'library/feedback.html', get_user_and_send_feedback(request))


