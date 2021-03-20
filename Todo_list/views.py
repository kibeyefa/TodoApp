from django.shortcuts import render, get_object_or_404
from Todo_list.models import Task
from .forms import MyForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    if len(tasks) == 0:
        empty = True
    else:
        empty = False

    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = MyForm()
    return render(request, "Todo_list/index.html", {
        "tasks":tasks,
        "empty": empty,
        "form": form})


def delete(request, pk=None):
    task = get_object_or_404(Task, pk=pk)
    task.instance = task
    task.delete()

    return HttpResponseRedirect("/")