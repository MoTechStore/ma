from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse
from kye.models import Task
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .forms import TaskForm
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from . import models
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime


class Deadline():
    def day(request, pk):
        task_days = Task.objects.values_list('task_days').filter( id = pk)
        created_at = Task.objects.values_list('created_at').filter( id = pk)
        task_deadline = Task.objects.values_list('task_deadline').filter( id = pk)
        today_date = datetime.today().strftime('%Y,%m,%d')


        print("Task Days")
        print(task_days)

        
        # Calculating number of deadline days
        a = str(created_at)
        b = str(task_deadline)
        print(pk)
        print(a)
        print(b)

        # Slicing Created Day
        da = len(a)

        print(da)

        if da == 51:
            x = a[30:40]
            print(x)
        elif da == 52:
            x = a[30:41]
            print(x)
        elif da == 53:
            x = a[30:42]
            print(x)
        else:
            print("Nothing")

        print("New Created Date", x)


        de = len(b)

        print(de)

        if de == 51:
            y = b[30:40]
            print(y)
        elif de == 52:
            y = b[30:41]
            print(x)
        elif de == 53:
            y = b[30:42]
            print(y)
        else:
            print("Nothing")

        print("New Deadline Date", y)

       
        print("Created Date", x)
        print("Deadline Date", y)
        date_time_str = x
        date_time_str2 = y

        print(date_time_str)
        print(date_time_str2)
        print(type(date_time_str))
        print(type(date_time_str2))
        
        myTime = datetime.strptime(date_time_str, "%Y, %m, %d")
        myTime2 = datetime.strptime(date_time_str2, "%Y, %m, %d")
        print(type(myTime))
        print(type(myTime2))

        myFormat = "%Y,%m,%d"

        print("Original Reg Date", myTime)
        new_created_at = myTime.strftime(myFormat)
        print("New Reg Date", new_created_at)

        print("Original Exit Date", myTime2)
        new_task_deadline = myTime2.strftime(myFormat)
        print("New Exit Date", new_task_deadline)

        print(type(new_created_at))

        d2 = myTime2.date()
        d1 = myTime.date()
        delta = d2 - d1
        print(delta)
        print(delta.days)
        mo = delta.days
        print("Differences in date is ", mo)
        print(type(mo))

        Task.objects.filter(id = pk).update(days_counter = mo)

        print(task_days)
        task_days = str(task_days)
        limit_date = len(task_days)
        print("Length")
        print(limit_date)


        if limit_date == 17:
           task_days = task_days[12:13]
           print(task_days)
        elif limit_date == 18:
           task_days = task_days[12:14]
           print(task_days)
        elif limit_date == 19:
            task_days = task_days[12:15]
            print(task_days)
        else:
            print("Nothing")

        task_days = int(task_days)    
        print("Data Types")    
        print(type(mo))
        print(type(task_days))

        if mo == task_days:
            Task.objects.filter(id = pk).update(status = "completed")
            print("Task Is Completed")
        elif mo > task_days:
            Task.objects.filter(id = pk).update(status = "deadline")
            days_exceed = mo - task_days
            print("Task Is In Deadline")
            print("Days Exceeded", days_exceed)
        else:
            Task.objects.filter(id = pk).update(status = "pending")
            print("Task Is Pending")
         
        # Adding number of days a car parked
        return redirect('pending')



def dashboard(request):
    return render(request, 'dashboard/admin/home.html')


def addcase_form(request):
    return render(request, 'dashboard/admin/add_case.html')

def index(request):
    return render(request, 'dashboard/admin/login.html')


def home(request):
    return render(request, 'dashboard/users/home.html')


def comp(request):
    return render(request, 'dashboard/users/comp_reg.html')    






def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_superuser or user.is_admin:
                return redirect('dashboard')
            elif user.is_officer:
                return redirect('home')
            else:    
                return redirect('index')                 
        else:
            messages.info(request,"Invalid username or password")
            return redirect('index')    



def logout_view(request):
    logout(request)
    return redirect('/')



def publish_case(request):
    if request.method == 'POST':
        report = ''
        task_title = request.POST['task_title']
        task_customer = request.POST['task_customer']
        supervisor = request.POST['supervisor']
        task_desc = request.POST['task_desc']
        task_days = request.POST['task_days']
        amount = request.POST['amount']
        modus = request.POST['modus']
        suspect = request.POST['suspect']
        comment = request.POST['comment']
        task_deadline = request.POST['task_deadline']
        current_user = request.user
        user_id = current_user.id
        username = current_user.username
        print(username)
        print(user_id)
        publisher_id = user_id
        status = "pending"
        created_at = datetime.today().strftime('%Y-%m-%d')
        print(created_at)
        print("Dead Line")
        print(task_deadline)
        print(type(task_deadline))

        if len(request.FILES) != 0:
            report = request.FILES['report']
            a = Task(task_title=task_title, task_customer=task_customer, supervisor=supervisor, amount=amount, 
            task_desc=task_desc, task_deadline=task_deadline, report=report, publisher_id=publisher_id, status=status, created_at=created_at, task_days=task_days)
            a.save()
            return redirect('task_list')
        elif len(request.FILES) == 0:
            a = Task(task_title=task_title, task_customer=task_customer, supervisor=supervisor, amount=amount, 
            task_desc=task_desc, task_deadline=task_deadline, report=report, publisher_id=publisher_id, status=status, created_at=created_at, task_days=task_days)
            a.save()
            return redirect('task_list')
        else:
            return redirect('dashboard')
         

class UserView(generic.ListView):
    model = User
    template_name = 'dashboard/admin/list_users.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        return User.objects.order_by('-id')



def delete_task(request, pk):
    if request.method == 'POST':
        task = Task.objects.get(pk=pk)
        task.delete()
        messages.success(request, 'Data was deleted successfully!')
    return redirect('manage-tasks')


class TaskListView(generic.ListView):
    model = Task
    template_name = 'dashboard/admin/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 3


    def get_queryset(self):
        return Task.objects.all()


class Pending(generic.ListView):
    model = Task
    template_name = 'dashboard/admin/pending.html'
    context_object_name = 'tasks'
    paginate_by = 3


    def get_queryset(self):
        return Task.objects.all().filter(status="pending")      


class Completed(generic.ListView):
    model = Task
    template_name = 'dashboard/admin/completed.html'
    context_object_name = 'tasks'
    paginate_by = 3


    def get_queryset(self):
        return Task.objects.all().filter(status="completed")



class SearchResults(ListView):
    model = Task
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(task_title__icontains=query) | Q(task_desc__icontains=query)
        )
        return object_list

class UploadTask(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    template_name = 'dashboard/admin/add_task.html'


   
def book_list(request):
    tasks = Task.objects.all()
    return render(request, 'dashboard/admin/class_task_list.html', {
        'tasks': tasks
    })



class ManageTask(ListView):
    model = Task
    template_name = 'dashboard/admin/manage_task.html'
    context_object_name = 'tasks'



def add_quote(request):
	if request.method == "POST":
		form = InspirationalQuoteForm(
			data=request.POST,
			files=request.FILES,
		)

		if form.is_valid():
			quote = form.save()
			return redirect("add_quote")
		else:
			form = InspirationalQuoteForm()
			return render(request, "dashboard/admin/change_quote.html",{"form": form})
	else:
		form = InspirationalQuoteForm()
		return render(request, "dashboard/admin/change_quote.html",{"form": form})		



def download_quote_picture(request, quote_id):
	quote = get_object_or_404(InspirationalQuote, pk=quote_id)
	file_name, file_extension = os.path.splitext(quote.picture.file.name)
	file_extension = file_extension[1:] # remove the dot
	response = FileResponse(quote.picture.file, content_type="image/%s" % file_extension)
	response["Content-Disposition"] = "attachment;" \
	" filename=%s---%s.%s" % (
		slugify(quote.author)[:100],
		slugify(quote.quote)[:100],
		file_extension)
	return response


class TaskView(DetailView):
    model = Task


class DeleteTask(SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('manage-tasks')
    success_message = "Data successfully deleted"


class UpdateTask(SuccessMessageMixin, UpdateView): 
    model = Task
    form_class = TaskForm
    template_name = 'dashboard/admin/edit_task.html'
    success_url = reverse_lazy('manage-tasks')
    success_message = "Data successfully updated"



# User view
def add_case(request):
    return render(request, 'dashboard/user/add_case.html')

def user_dashboard(request):
    return render(request, 'dashboard/user/home.html')

def u_upload(request):
    if request.method == 'POST':
        task_title = request.POST['task_title']
        task_phases = request.POST['task_phases']
        task_category = request.POST['task_category']
        task_customer = request.POST['task_customer']
        task_owner = request.POST['task_owner']
        task_revenue = request.POST['task_revenue']
        task_desc = request.POST['task_desc']
        task_deadline = request.POST['task_deadline']
        report = request.FILES['report']
        invoice = request.FILES['invoice']

        a = Task(task_title=task_title, task_phases=task_phases,
         task_category=task_category, task_customer=task_customer, 
         task_owner=task_owner, task_revenue=task_revenue, 
         task_desc=task_desc, task_deadline=task_deadline, report=report, invoice=invoice)
        a.save()
        return redirect('u_tasklist')
    else:
        return redirect('user_dashboard')


class UTaskListView(generic.ListView):
    model = Task
    template_name = 'dashboard/user/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 8

    def get_queryset(self):
        return Task.objects.all()



"""
def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(task_title__icontains=query) | Q(task_desc__icontains=query)
            results= Task.objects.filter(lookups).distinct()
            context={'results': results,'submitbutton': submitbutton}
            return render(request, 'dashboard/admin/search.html', context)
        else:
            return render(request, 'dashboard/admin/search.html')
    else:
        return render(request, 'dashboard/admin/search.html')
"""

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

    if query is None:
        return redirect('dashboard')
    else:
                # First word
                qs1 =models.Task.objects.all().filter(task_title__icontains=query)
                #qs2 =models.Task.objects.all().filter(publisher__icontains=query)
                qs3 =models.Task.objects.all().filter(status__icontains=query)
                qs4 =models.Task.objects.all().filter(supervisor__icontains=query)
                qs5 =models.Task.objects.all().filter(comment__icontains=query)
                qs6 =models.Task.objects.all().filter(modus__icontains=query)
                qs7 =models.Task.objects.all().filter(task_customer__icontains=query)
                qs8 =models.Task.objects.all().filter(task_desc__icontains=query)

                files = itertools.chain(qs1,qs3, qs4, qs5, qs6, qs7, qs8)

                res = []
                for i in files:
                    if i not in res:
                        res.append(i)

                # word variable will be shown in html when user click on search button
                word="Searched Result :"

                print(res)
                files = res

                page = request.GET.get('page', 1)
                paginator = Paginator(files, 10)
                try:
                    files = paginator.page(page)
                except PageNotAnInteger:
                    files = paginator.page(1)
                except EmptyPage:
                    files = paginator.page(paginator.num_pages)   

                if files:
                    return render(request,'dashboard/admin/result.html',{'files':files,'word':word})
                return render(request,'dashboard/admin/result.html',{'files':files,'word':word})