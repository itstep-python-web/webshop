from django.shortcuts import render


def reg(request):
    return render(request, 'accounts/reg.html')


def entry(request):
    return render(request, 'accounts/entry.html')


def logout(request):
    return render(request, 'accounts/logout.html')


