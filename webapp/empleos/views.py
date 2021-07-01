from django.shortcuts import render
from django.contrib import messages
from .forms import EditJobForm, NewJobForm,ApplyJobForm
from core.decorators import user_is_organizacion, user_is_persona
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from cuentas.models import User
from organizaciones.models import OrgProfile
from django.shortcuts import render, redirect, get_object_or_404
from .models import Jobs, Applicants
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView,FormView
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail

@method_decorator(user_is_organizacion, name="dispatch")
class JobCreateView(LoginRequiredMixin,CreateView):
    template_name = "empleos/register.html"
    form_class = NewJobForm
    extra_context = {"title": "Post New Job"}
    success_url = reverse_lazy("empleos:job-list")
    
    def form_valid(self, form):
        form.instance.organizacion = self.request.user.orgprofile
        #messages.success(self.request, "Job created successfully")
        send_mail(
                'Nueva Oportunidad para Revisión',
                'Una nueva oportunidad a sido registrada para revisión',
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
                )
        return super(JobCreateView, self).form_valid(form)

@method_decorator(user_is_organizacion, name="dispatch")
class JobUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "empleos/edit.html"
    form_class = EditJobForm
    success_url = reverse_lazy("empleos:job-list")
    
    context_object_name = "jobs"
    def get_queryset(self):
        return Jobs.objects.all()

@method_decorator(user_is_organizacion, name="dispatch")
class JobListView(LoginRequiredMixin,ListView):

    model = Jobs
    template_name="empleos/jobs_list.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return self.model.objects.filter(organizacion_id=self.request.user.orgprofile)
    

@method_decorator(user_is_organizacion, name="dispatch")
class JobDeleteView(LoginRequiredMixin,DeleteView):
    # specify the model you want to use
    model = Jobs
     
    # can specify success url
    # url to redirect after sucessfully
    # deleting object
    success_url = reverse_lazy("core:dashboard")

class JobDetailView(LoginRequiredMixin,DetailView):
    # specify the model to use
    model = Jobs
    template_name="empleos/jobs_detail.html"
    context_object_name = "job"

class SearchView(ListView):
    model = Jobs
    template_name = "empleos/search.html"
    context_object_name = "jobs"

    def get_queryset(self):
        # q = JobDocument.search().query("match", title=self.request.GET['position']).to_queryset()
        # print(q)
        # return q
        return self.model.objects.filter(
            ciudad__contains=self.request.GET.get("ciudad"),
            titulo__contains=self.request.GET.get("titulo"),
            tipo__contains=self.request.GET.get("tipo")
            ) 
class ApplyJobView(CreateView):
    model = Applicants
    form_class = ApplyJobForm
    slug_field = "job_id"
    slug_url_kwarg = "job_id"
    template_name = 'empleos/applicants_form.html' 

    def get_context_data(self,*args, **kwargs):
        context = super(ApplyJobView, self).get_context_data(*args,**kwargs)
        context['applicants'] = Applicants.objects.filter(applicant_id=self.request.user.id,job_id=self.kwargs["job_id"])
        if context["applicants"]:
            return context
        else:
            context["applicants"]="None"
            return context
    
    @method_decorator(login_required(login_url=reverse_lazy("core:login")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
            # check if user already 
        print("///validadion///")
        aplicante=Applicants.objects.filter(applicant_id=self.request.user.id,job_id=self.kwargs["job_id"])
        print(aplicante)
        job=Jobs.objects.filter(id=self.kwargs["job_id"])
        print("///job///",job)
        #applicante = Applicants.objects.filter(user=self.request.user.id, job_id=self.kwargs["job_id"])
        if aplicante:
            messages.info(self.request, "La aplicación ya se realizó")
            return HttpResponseRedirect(reverse_lazy("core:home"))
        # save applicant
        print("aún no aplica")
        form.instance.applicant = self.request.user
       
        form.instance.job_id=self.kwargs["job_id"]
        form.save()
        print("guardado")
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        print("entra al post")
        form = self.get_form()
        if form.is_valid():
            messages.info(self.request, "Successfully applied for the job!")
            send_mail(
                'Oportunidad Notificación',
                'Aplicación exitosa ',
                'info@chamanaku.org',
                [self.request.user.email],
                fail_silently=False,
                )
            return self.form_valid(form)
        else:
            messages.info(self.request, "La aplicación ya se realizó")
            return HttpResponseRedirect('/core/home')

    def get_success_url(self):
        return reverse_lazy('core:home')

    # def get_form_kwargs(self):
    #     kwargs = super(ApplyJobView, self).get_form_kwargs()
    #     print(kwargs)
    #     kwargs['job'] = 1
    #     return kwargs

   


class ApplicantsListView(ListView):
    model = Applicants
    template_name = "empleos/all-applicants.html"
    context_object_name = "applicants"
    slug_field = "job_id"
    slug_url_kwarg = "job_id"

    @method_decorator(login_required(login_url=reverse_lazy("core:login")))
    #@method_decorator(user_is_persona)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        # jobs = Job.objects.filter(user_id=self.request.user.id)
        # return self.model.objects.filter(job__user_id=self.request.user.id)
        #print(self.request.user.id)
        print(self.kwargs["pk"])
       
        self.queryset = self.model.objects.filter(job=self.kwargs['pk'])
        
        applicantes=self.queryset
        for i in applicantes:
            print(i.applicant.first_name)
        
        return self.queryset