from django.contrib.auth import get_user
from django.shortcuts import get_object_or_404, redirect

from .models import Author, Book, Comment, Feedback


def get_user_and_form_context(request):
    context = {}
    context.update({'User': get_user(request)})
    return context


def get_user_books_and_form_context_with_filter(request):
    all_filters = {
        'technology': ['Python', 'Java', 'C++', 'JS', 'Others'],
        'difficulty': ['L', 'M', 'H'],
        'language': ['EN', 'RU']
    }
    if request.GET:
        all_filters = _confirm_filter(request, all_filters)
    all_books = Book.objects.filter(technology__in=all_filters['technology'],
                                    difficulty__in=all_filters['difficulty'],
                                    language__in=all_filters['language'])
    user = get_user(request)
    context = {
        'Books': all_books,
        'User': user,
    }
    return context


def get_user_book_and_form_context(request, book_id):
    if request.method == 'POST':
        _post_new_comment(request, book_id)
    user = get_user(request)
    certain_book = get_object_or_404(Book, pk=book_id)
    comments = Comment.objects.filter(book_id=book_id)
    context = {
        'Book': certain_book,
        'User': user,
        'Comments': comments,
    }
    return context


def get_user_authors_and_form_context(request):
    user = get_user(request)
    authors = Author.objects.all()
    context = {
        'User': user,
        'Authors': authors,
    }
    return context


def get_user_author_and_form_context(request, author_id):
    user = get_user(request)
    certain_author = get_object_or_404(Author, pk=author_id)
    context = {
        'Author': certain_author,
        'User': user,
    }
    return context


def get_user_and_send_feedback(request):
    user = get_user(request)
    context = {
        'User': user,
    }
    if request.method == 'POST':
        if user.is_anonymous:
            new_feedback = Feedback.objects.create(name=request.POST['name'], email=request.POST['email'],
                                                   feed=request.POST['feed'])
        else:
            new_feedback = Feedback.objects.create(name=user.username, email=user.email, feed=request.POST['feed'])
        new_feedback.save()
        context.update({'Success': 'Фидбэк успешно отправлен!!!'})
    return context


def _post_new_comment(request, book_id):
    comment = Comment.objects.create(user_name=get_user(request),
                                     book_id=book_id,
                                     comment_body=request.POST.get('comment'))
    comment.save()
    return redirect('library:certain_book', book_id)


def _confirm_filter(request, all_filters):
    request_dictionary = dict(request.GET)
    request_dictionary.pop('submit')
    for i in request_dictionary:
        all_filters.update({i: request_dictionary[i]})
    return all_filters