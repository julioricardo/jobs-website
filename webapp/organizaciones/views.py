from django.shortcuts import render
from .forms import OrgEditForm
from .models import OrgProfile
from cuentas.models import User
from core import decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from core.decorators import user_is_organizacion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
# Create your views here.





@login_required
@decorators.user_is_organizacion
def edit(request):
    if request.method == 'POST':
        usuario=request.user
        role=request.user.role
        print("usuario:",usuario,role)
        if role=="organizacion":
            perfil=OrgProfile.objects.filter(user=usuario).first()
            org_form = OrgEditForm(request.POST, request.FILES, instance=perfil)
        if org_form.is_valid():
            org_form.save()
            
    else:
        usuario=request.user
        perfil=OrgProfile.objects.filter(user=usuario).first()
        org_form = OrgEditForm(instance=perfil)
        
    context = {
        'form': org_form,
    }
    return render(request, 'organizaciones/org_edit.html', context=context)


@method_decorator(user_is_organizacion, name="dispatch")
class OrgDetailView(LoginRequiredMixin,ListView):
    
    model = OrgProfile
    template_name="organizaciones/org_detail.html"
    context_object_name = "orgprofile"
    
    def get_queryset(self):
        user=self.request.user
        print("usuario**:",user)
        return OrgProfile.objects.filter(user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    #def get_queryset(self):
    #    return self.model.objects.filter(user_id=self.request.user.id)
    #paginate_by = 100  # if pagination is desired
@method_decorator(user_is_organizacion, name="dispatch")
class OrgListView(LoginRequiredMixin,ListView):
    
    model = OrgProfile
    template_name="organizaciones/org_list.html"
    context_object_name = "orgprofile"
    def get_queryset(self):
        user=self.request.user
        print("usuario**:",user)
        return OrgProfile.objects.filter(user=self.request.user.id)
    