from django.shortcuts import get_object_or_404, redirect, render

from .models import TodoItem


def todo_list(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "add":
            title = request.POST.get("title", "").strip()
            if title:
                prefix = getattr(request, "todo_title_prefix", "default")
                TodoItem.objects.create(title=title, prefix=prefix)
        elif action == "toggle":
            todo = get_object_or_404(TodoItem, pk=request.POST.get("todo_id"))
            todo.completed = not todo.completed
            todo.save(update_fields=["completed"])
        elif action == "delete":
            todo = get_object_or_404(TodoItem, pk=request.POST.get("todo_id"))
            todo.delete()

        return redirect("todo-list")

    todos = TodoItem.objects.order_by("completed", "-created_at")
    return render(
        request,
        "myapp/todo_list.html",
        {
            "todos": todos,
            "request_source": getattr(request, "todo_source", "browser"),
            "request_prefix": getattr(request, "todo_title_prefix", "default"),
        },
    )

