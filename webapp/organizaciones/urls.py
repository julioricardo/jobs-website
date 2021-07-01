from django.urls import path
from .views import edit, OrgDetailView, OrgListView

app_name = 'organizaciones'

urlpatterns = [
path('edit/', edit, name='edit-org'),
path('<pk>/', OrgDetailView.as_view(template_name='organizaciones/org_detail.html'),name='detail-org'),
path('', OrgListView.as_view(template_name='organizaciones/org_list.html'), name='org-list'),
]