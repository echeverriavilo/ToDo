from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView
from ..models import Task

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        week_end = today + timezone.timedelta(days=7)
        if self.request.user.is_authenticated:
            context['tasks'] = Task.objects.filter(user=self.request.user, due_date__range=(today, week_end))
        else:
            context['tasks'] = Task.objects.none()  # No mostrar tareas si el usuario no está autenticado
        
        return context
    