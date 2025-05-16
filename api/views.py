from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# List all tasks
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# Show task details
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

# Create a new task
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Update an existing task
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

# Delete a task
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
