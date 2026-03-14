from django.urls import path
from .views import *

app_name = 'cars'

urlpatterns = [

    path('', CarListView.as_view(), name='car-list'),
    path('create/', CarCreateView.as_view(), name='car-create'),
    path('<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),

    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand-create'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('brands/<int:pk>/update/', BrandUpdateView.as_view(), name='brand-update'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand-delete'),

    path('features/', FeatureListView.as_view(), name='feature-list'),
    path('features/create/', FeatureCreateView.as_view(), name='feature-create'),
    path('features/<int:pk>/', FeatureDetailView.as_view(), name='feature-detail'),
    path('features/<int:pk>/update/', FeatureUpdateView.as_view(), name='feature-update'),
    path('features/<int:pk>/delete/', FeatureDeleteView.as_view(), name='feature-delete'),
]