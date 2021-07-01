from django.urls import path
from .views import edit

from .views import ProfileDetailView, ProfileListView

app_name = 'cuentas'
urlpatterns = [
path('edit/', edit, name='edit-profile'),
path('<pk>/', ProfileDetailView.as_view(template_name='cuentas/profile_detail.html'),name='detail-profile'),
path('', ProfileListView.as_view(template_name='cuentas/profile_list.html'), name='profile-list'),
]