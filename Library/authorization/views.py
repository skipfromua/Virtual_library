from django.shortcuts import render, redirect
from .services import authenticate_and_login_user, logout


def logout_view(request):
    logout(request)
    return redirect('library:main')

def login_view(request):
    if request.method == 'POST':
        message, context = authenticate_and_login_user(request)
        if message:
            return redirect('library:main')
        else:
            return render(request, 'authorization/authentication.html', context)
    else:
        return render(request, 'authorization/authentication.html')

