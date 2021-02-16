from django.contrib import admin
from django.urls import path
# from django.views.generic import TemplateView
from .views import List, Details,Create,Edit,Delete
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list', login_required(List.as_view(template_name="index.html")),name='list'),
    path('details/<int:pk>', login_required(Details.as_view(template_name="details.html")), name='details'),
    path('create', login_required(Create.as_view(template_name="create.html")), name='create'),
    path('edit/<int:pk>', login_required(Edit.as_view(template_name="edit.html")), name='edit'),
    path('delete/<int:pk>', login_required(Delete.as_view()), name='delete'),
]
