from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
# Create your views here.
from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.forms import UserRegistration, UserEditForm
from django.core.paginator import Paginator
from django.http import HttpResponse
from empleos.models import Jobs
from core.decorators import user_is_organizacion, user_is_persona
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
# Create your views here.
"""
def homeview(request):
    job_list = Jobs.objects.all()
    paginator = Paginator(job_list, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/list.html', {'page_obj': page_obj})
"""


class HomeView(ListView):
    
   
    model = Jobs
    template_name = "home2.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return self.model.objects.filter(activo="True")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["trendings"] = self.model.objects.unfilled(created_at__month=timezone.now().month)[:3]
        return context


@method_decorator(user_is_organizacion, name="dispatch")
class orgdashboard(LoginRequiredMixin,ListView):
    model = Jobs
    template_name = "core/dashboard2.html"
   
    context_object_name = "jobs"
  
    def get_queryset(self):
        
        return self.model.objects.filter(organizacion_id=self.request.user.orgprofile)
        
  




def Organizacionregister(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.role="organizacion"
            new_user.save()
            return render(request, 'core/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'core/register.html', context=context)

