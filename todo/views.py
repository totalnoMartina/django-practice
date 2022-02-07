from django.shortcuts import render, redirect
from .models import Item


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
    return render(request, 'todo/add_item.html')
