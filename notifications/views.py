from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notification


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications/list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user).order_by('-created_at')
        qs.filter(is_read=False).update(is_read=True)
        return qs