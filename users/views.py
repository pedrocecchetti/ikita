from django.http import HttpRequest, HttpResponse
from django.contrib.auth import aauthenticate, alogin, alogout
from users.forms.login import LoginForm
from django.shortcuts import render, redirect


async def login_view(request: HttpRequest) -> HttpResponse:
    user = await request.auser()
    if user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = await aauthenticate(
                request=request, username=form.cleaned_data['email'], password=form.cleaned_data['password']
            )
            await alogin(request, user)
            # process the data in form.cleaned_data
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


async def logout_view(request: HttpRequest) -> HttpResponse:
    user = await request.auser()
    if user.is_authenticated:
        await alogout(request)

    return redirect('homepage')


async def dashboard_view(request: HttpRequest) -> HttpResponse:
    user = await request.auser()

    if not user.is_authenticated:
        print('SHOW')
        return redirect('login')
    return render(request, 'dashboard.html', {'user': user})
