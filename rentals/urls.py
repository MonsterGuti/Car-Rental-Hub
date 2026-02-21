from django.urls import path

from rentals.views import RentalListView, RentalDetailView, RentalCreateView, RentalUpdateView, RentalDeleteView

app_name = 'rentals'
urlpatterns = [
    path('', RentalListView.as_view(), name='list'),
    path('<int:pk>/', RentalDetailView.as_view(), name='detail'),
    path('create/', RentalCreateView.as_view(), name='create'),
    path('<int:pk>/update/', RentalUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', RentalDeleteView.as_view(), name='delete'),
]
