from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse

from .forms import LoginForm


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse(Mail))
                else:
                    return HttpResponse('')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def Mail(request):
    return render(request, 'login/mail.html', {})


def razv(request):
    return render(request, 'login/razv.html', {})


def kor(request):
    return render(request, 'login/kor.html', {})


def chit(request):
    return render(request, 'login/chit.html', {})


def rass(request):
    return render(request, 'login/rass.html', {})


def spam(request):
    return render(request, 'login/spam.html', {})


def kor2(request):
    return render(request, 'login/kor2.html', {})