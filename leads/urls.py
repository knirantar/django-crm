from django.contrib import admin
from django.urls import path
from leads.views import (
    home_page,lead_detail,lead_create,lead_update,lead_delete,LeadListView,LeadDetailView,
    LeadCreateView,LeadUpdateView,LeadDeleteView)
app_name = 'leads'
urlpatterns = [
    path('',LeadListView.as_view(),name = 'home'),
    path('create/',LeadCreateView.as_view(),name = 'lead-create'),
    path('<int:pk>/',LeadDetailView.as_view(),name = 'lead-detail'),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name = 'lead-update'),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name = 'lead-delete'),
]
