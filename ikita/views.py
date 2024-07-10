from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect


async def homepage_view(request: HttpRequest) -> HttpResponse:
    user = await request.auser()
    if user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'homepage.html')
