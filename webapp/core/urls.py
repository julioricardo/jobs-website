from django.urls import path
from core.views.organizacion import orgdashboard,Organizacionregister,HomeView
from core.views.persona import edit, Personaregister
from core.views.registro import home
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)

app_name = 'core'

urlpatterns = [
    path('inicio', home, name='start'),
    path('home/', HomeView.as_view(template_name='core/home2.html'), name='home'),
    path('register/', Personaregister, name='persona-register'),
    path('orgregister/', Organizacionregister, name='organizacion-register'),
    path('edit/', edit, name='edit'),
    path('dashboard/', orgdashboard.as_view(template_name='core/dashboard2.html'), name='dashboard'),
    path('', LoginView.as_view(template_name='core/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='core/password_change_form.html'), name='password_change'),
    path('password_change/dond/', PasswordChangeDoneView.as_view(template_name='core/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='core/password_reset_form.html',
        email_template_name='core/password_reset_email.html',
        success_url=reverse_lazy('core:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='core/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='core/password_reset_confirm.html',
        success_url=reverse_lazy('core:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='core/password_reset_complete.html'), name='password_reset_complete'),

]