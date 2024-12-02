from django.shortcuts import render ,redirect
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
import json

# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False) #commit for delaying the saving
            instance.manager = request.user 
            instance.save()
            messages.success(request,('New task added'))
      
        return redirect('todolist')
    else : 
       all_tasks = TaskList.objects.filter(manager=request.user)
       paginator = Paginator(all_tasks, 5)
       page = request.GET.get('page')
       all_tasks = paginator.get_page(page)
       return render(request, 'todolist.html',{'all_tasks' : all_tasks})
   
@login_required
def delete_task(request, task_id):
    
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
       task.delete()
    else:
       messages.error(request,('Access restricted, You are not allowed!'))
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST or None, instance= task)
        if form.is_valid():  
            form.save()      
            messages.success(request,('Task Edited'))
        return redirect('todolist')
    else : 
       task_obj = TaskList.objects.get(pk=task_id)
       return render(request, 'edit.html',{'task_obj' : task_obj})


def index(request):
    all_tasks = TaskList.objects.all()
    count = 0
    for obj in all_tasks:
        if obj.done:
            count += 1  

    context = {
        'counted_completed_task': 'Completed Tasks: ' + str(count)  
    }
    return render(request, 'index.html',context)


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
      task.done = True
      task.date_done = now()
      task.save()
    else : 
        messages.error(request,('Access restricted, You are not allowed!'))
    return redirect('todolist')



@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.date_done = None 
    task.save()
    return redirect('todolist')

def analytics(request):
    all_tasks = TaskList.objects.all()
    count = 0
    for obj in all_tasks:
        if obj.done:
            count += 1  
    non_count = len(all_tasks) - count
    context = {
        'labels':['Unfinished tasks: '+str(non_count),'Finished tasks: '+ str(count)] , 
        'data': [non_count,count],
    }
    
  
    context_json = json.dumps(context)
    return render(request, 'analytics.html',{'chart_data':context_json })

def about(request):
    context = {
        'about_text':'Welcome to about page.'
    }
    return render(request, 'about.html',context)