from django.urls import path
from common.views import HomeView, AddReviewView, DashboardView, ReviewListView

app_name = 'common'
# common/urls.py
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cars/<int:car_pk>/review/', AddReviewView.as_view(), name='add-review'),
    path('review/add/', AddReviewView.as_view(), name='add-review-general'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
