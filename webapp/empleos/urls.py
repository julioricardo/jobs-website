from django.urls import path

from .views import JobCreateView, JobListView, JobUpdateView, JobDeleteView, JobDetailView, SearchView, ApplyJobView,ApplicantsListView
from django.urls import reverse_lazy

app_name = 'empleos'
urlpatterns = [
    path("register/", JobCreateView.as_view(template_name='empleos/register.html'), name="create-job"),
    path('', JobListView.as_view(template_name='empleos/job_list.html'), name='job-list'),
    path("all-applicants/<int:pk>/",ApplicantsListView.as_view(template_name='empleos/all-applicants.html'),name="employer-all-applicants"),         
    path('edit/<int:pk>/', JobUpdateView.as_view(template_name='empleos/edit.html'), name='update-job'),
    path('<pk>/delete/', JobDeleteView.as_view(),name='delete-job'),
    path("search/", SearchView.as_view(template_name='empleos/search.html'), name="search"),
    path('<pk>/', JobDetailView.as_view(template_name='empleos/jobs_detail.html'),name='detail-job'),
    path("apply-job/<int:job_id>/", ApplyJobView.as_view(), name="apply-job"),
]
    
