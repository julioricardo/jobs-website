from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Profile
from cuentas.forms import EditForm
from core import decorators

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from core.decorators import user_is_organizacion, user_is_persona
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

@login_required
@decorators.user_is_persona
def edit(request):
    if request.method == 'POST':
        #perfil=Profile.objects.filter(user=usuario).first()
        usuario=request.user
        role=request.user.role
        
        print("usuario:",usuario,role)
        if role=="persona":
            perfil=Profile.objects.filter(user=usuario).first()
            #perfil=get_object_or_404(Profile)
            org_form = EditForm(request.POST, request.FILES, instance=perfil)
        if org_form.is_valid():
            org_form.save()
    else:
        usuario=request.user
        perfil=Profile.objects.filter(user=usuario).first()
        org_form = EditForm(instance=perfil)
    context = {
        'form': org_form,
    }
    return render(request, 'cuentas/profile_edit.html', context=context)

@method_decorator(user_is_persona, name="dispatch")
class ProfileDetailView(LoginRequiredMixin,ListView):
    
    model = Profile
    template_name="cuentas/profile_detail.html"
    context_object_name = "profile"
    
    def get_queryset(self):
        user=self.request.user
        print("usuario**:",user)
        return Profile.objects.filter(user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    #def get_queryset(self):
    #    return self.model.objects.filter(user_id=self.request.user.id)
    #paginate_by = 100  # if pagination is desired

@method_decorator(user_is_persona, name="dispatch")
class ProfileListView(LoginRequiredMixin,ListView):
   
    model = Profile
    template_name="cuentas/profile_list.html"
    context_object_name = "profile"
    def get_queryset(self):
        user=self.request.user
        
        print("usuario**:",user)
        return Profile.objects.filter(user=self.request.user.id)