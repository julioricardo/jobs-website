from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        if request.user.role=="organizacion":
            return redirect('core:dashboard')
        elif request.user.role=="persona":
            return redirect('core:home')
    return redirect('core:home')