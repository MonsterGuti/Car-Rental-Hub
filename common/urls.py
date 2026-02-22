from django.urls import path
from common.views import HomeView, AddReviewView, DashboardView

app_name = 'common'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cars/<int:pk>/review/', AddReviewView.as_view(), name='add-review'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
