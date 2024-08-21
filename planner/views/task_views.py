from django.db.models.base import Model as Model
from django.views.generic import ListView, DetailView,  DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from ..models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user).order_by('due_date')
        else:
            return Task.objects.none()

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'