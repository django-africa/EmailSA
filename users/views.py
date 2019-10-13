from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('user')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'nosignup.html')