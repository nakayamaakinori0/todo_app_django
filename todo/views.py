from django.shortcuts import render
from .models import TodoItem

# Create your views here.


def todo_list(request):
    print("### todo_list")
    todos = TodoItem.objects.all()
    print("todos:", todos)
    return render(request, "todo/todo_list.html", {"todos": todos})


def todo_create(request):
    print("### todo_create")
    if request.method == "POST":
        title = request.POST["title"]
        todo = TodoItem.objects.create(title=title)
        return redirect("todo_list")
    return render(request, "todo/todo_create.html")


def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        todo.title = request.POST["title"]
        todo.completed = "completed" in request.POST
        todo.save()
        return redirect("todo_list")
    return render(request, "todo/todo_update.html", {"todo": todo})
