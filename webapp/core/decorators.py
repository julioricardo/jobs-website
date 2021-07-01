from django.core.exceptions import PermissionDenied


def user_is_persona(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            if user.role == "persona":
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
                raise PermissionDenied
    return wrap


def user_is_organizacion(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            if user.role == "organizacion":
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
                raise PermissionDenied
    return wrap