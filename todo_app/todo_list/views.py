from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item added to your list!!'))
            return render(request, 'home.html', {'items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'items': all_items})

def about(request):
    return render(request, 'about.html', {})

def delete(request, id):
    item = List.objects.get(pk = id)
    item.delete()

    messages.success(request, ('Item has been deleted!!'))
    return redirect('todo_list:home')

def crossOff(request, id):
    item = List.objects.get(pk = id)
    item.completed = True
    item.save()

    return redirect('todo_list:home')

def uncross(request, id):
    item = List.objects.get(pk = id)
    item.completed = False
    item.save()

    return redirect('todo_list:home')

def edit(request, id):
    if request.method == 'POST':
        item = List.objects.get(pk=id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited!!'))
            return redirect('todo_list:home')

    else:
        item = List.objects.get(pk = id)
        return render(request, 'edit.html', {'item': item})