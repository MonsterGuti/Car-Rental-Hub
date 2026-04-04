from django.urls import path

from common.api_views import ReviewListCreateApiView
from common.views import HomeView, AddReviewView, DashboardView, ReviewListView, EditReviewView, DeleteReviewView

app_name = 'common'
# common/urls.py
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('reviews/api/', ReviewListCreateApiView.as_view(), name='review-list'),
    path('cars/<int:car_pk>/review/', AddReviewView.as_view(), name='add-review'),
    path('review/add/', AddReviewView.as_view(), name='add-review-general'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('review/edit/<int:pk>/', EditReviewView.as_view(), name='edit-review'),
    path('review/delete/<int:pk>/', DeleteReviewView.as_view(), name='delete-review'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
