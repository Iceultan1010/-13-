from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Қош келдіңіз, {user.username}! Тіркелу сәтті аяқталды.')
            return redirect('home')
        else:
            messages.error(request, 'Тіркелу кезінде қате орын алды. Деректерді тексеріңіз.')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Қош келдіңіз, {user.username}!')
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            messages.error(request, 'Пайдаланушы аты немесе құпия сөз қате.')

    return render(request, 'accounts/login.html', {'next': request.GET.get('next', '')})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Жүйеден сәтті шықтыңыз.')
    return redirect('home')
