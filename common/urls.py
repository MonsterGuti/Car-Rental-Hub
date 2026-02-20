from django.urls import path
from common.views import home_view, review_create_view

app_name = 'common'
urlpatterns = [
    path('', home_view, name='home'),
    path('review', review_create_view, name='review-create'),
]
