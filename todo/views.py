from django.shortcuts import render, redirect
from todo.models import Item


# Create your views here.


def get_todo_list(request):
    """ Rendering html document """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    """ Rendering items """
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done_status=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
