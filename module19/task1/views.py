from django.shortcuts import render
from django.http import HttpResponse
from .form import UserRegister
from .models import *

def platforms_templates(request):
    return render(request, 'platform.html')


def games_templates(request):
    Games=Game.objects.all()
    data = {
        'Games':Games,
    }
    return render(request, 'games.html', context=data)


def carts_templates(request):
    return render(request, 'cart.html')

def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in [b.name for b in users]:
                # byer = Buyer(name=username, age=age, balance='23')
                # byer.save()
                Buyer.objects.create(name=username, age=age, balance='23')
                return HttpResponse(f'Приветствуем , {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in [b.name for b in users]:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', context=info)