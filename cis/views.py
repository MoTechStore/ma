from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse
from cis.models import User, Task, Chat
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views import generic
#from django.contrib.auth.models import User
from .forms import TaskForm, ChatForm, UserForm
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from . import models
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.hashers import make_password
import django_excel as excel
from tablib import Dataset
from .resources import MosesResource
from rake_nltk import Rake
rake_nltk_var = Rake()






def import_data(request):
    result = ''
    if request.method == 'POST':
        file_format = request.POST['file-format']
        moses_resource = MosesResource()
        dataset = Dataset()
        new_task = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_task.read().decode('utf-8'),format='csv')
            result = moses_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_task.read().decode('utf-8'),format='json')
            # Testing data import
            result = moses_resource.import_data(dataset, dry_run=True) 

            if not result.has_errors():
                moses_resource.import_data(dataset, dry_run=False)

    return render(request, 'dashboard/admin/import.html')

    


# Investigation Officer Views
@login_required
def officer(request):
    pending = Task.objects.all().filter(status="pending").count()
    completed = Task.objects.all().filter(status="completed").count()
    all_case = Task.objects.all().count()

    context = {'pending':pending, 'completed':completed, 'all_case':all_case}
    return render(request, 'cis/dashboard/officer/home.html', context)


@login_required
def create_user(request):
    choice = ['1', '0', 'Officer', 'Admin', 'Manager']
    choice = {'choice': choice}
    if request.method == 'POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            userType=request.POST['userType']
            email=request.POST['email']
            password=request.POST['password']
            password = make_password(password)
            print("User Type")
            print(userType)
            if userType == "Officer":
                a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_cis_officer=True)
                a.save()
                messages.success(request, 'Member was created successfully!')
                return redirect('aluser')
            elif userType == "Admin":
                a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_superuser=True)
                a.save()
                messages.success(request, 'Member was created successfully!')
                return redirect('aluser')
            elif userType == "Manager":
                a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_cis_admin=True)
                a.save()
                messages.success(request, 'Member was created successfully!')
                return redirect('aluser')    
            else:
                messages.success(request, 'Member was not created')
                return redirect('create_user_form')
    else:
        return redirect('create_user_form')


class ADeleteUser(SuccessMessageMixin, DeleteView):
    model = User
    template_name='dashboard/admin/confirm_delete3.html'
    success_url = reverse_lazy('aluser')
    success_message = "Data successfully deleted"


class AEditUser(SuccessMessageMixin, UpdateView): 
    model = User
    form_class = UserForm
    template_name = 'cis/dashboard/admin/edit_user.html'
    success_url = reverse_lazy('aluser')
    success_message = "Data successfully updated"


class ALViewUser(DetailView):
    model = User
    template_name='cis/dashboard/admin/user_detail.html'


def create_user_form(request):
    choice = ['1', '0', 'Officer', 'Admin', 'Manager']
    choice = {'choice': choice}

    return render(request, 'cis/dashboard/admin/add_user.html', choice)




class Deadline():
    def day(request, pk):
        task_days = Task.objects.values_list('task_days').filter( id = pk)
        created_at = Task.objects.values_list('created_at').filter( id = pk)
        today_date = datetime.today().strftime('%Y, %m, %d')

        print("Task Days")
        print(task_days)

        a = str(created_at)
        print(pk)
        print(a)

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

        y = today_date
        date_time_str = x
        date_time_str2 = y

        print(date_time_str)
        print(date_time_str2)
        print(type(date_time_str))
        print(type(date_time_str2))
        
        myTime = datetime.strptime(date_time_str, "%Y, %m, %d")
        myTime2 = datetime.strptime(date_time_str2, "%Y, %m, %d")

        print("Data Type Below")
        print(type(myTime))
        print(type(myTime2))
        d1 = myTime.date()
        d2 = myTime2.date()

        delta = d2 - d1
        print(delta)
        print(delta.days)
        mo = delta.days
        print("Differences in date is ", mo)
        print(type(mo))
        print(task_days)
        print("Day Commited", task_days)

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
    
        print("Data Types")
        task_days = int(task_days)    
        print(type(mo))
        print(type(task_days))


        if mo == task_days:
            Task.objects.filter(id = pk).update(status = "completed")
            print("Task Is Completed")
        elif mo > task_days:
            Task.objects.filter(id = pk).update(status = "deadline")
            days_exceed = mo - task_days
            print("Task Is In Deadline")
            Task.objects.filter(id = pk).update(exceed_days = days_exceed)
            print("Days Exceeded", days_exceed)
        else:
            Task.objects.filter(id = pk).update(status = "pending")
            print("Task Is Pending")
         
        return redirect('pending')


@login_required
def userboard(request):
    deadline = Task.objects.all().filter(status="deadline").count()
    pending = Task.objects.all().filter(status="pending").count()
    completed = Task.objects.all().filter(status="completed").count()
    all_case = Task.objects.all().count()

    context = {'deadline':deadline, 'pending':pending, 'completed':completed, 'all_case':all_case}
    return render(request, 'cis/dashboard/admin/home.html', context)


@login_required
def addcase_form(request):
    return render(request, 'cis/dashboard/admin/add_case.html')

@login_required
def case_form(request):
    return render(request, 'cis/dashboard/officer/add_case.html')    

def index(request):
    return render(request, 'cis/dashboard/admin/login.html')

@login_required
def home(request):
    return render(request, 'cis/dashboard/users/home.html')

@login_required
def comp(request):
    return render(request, 'cis/dashboard/users/comp_reg.html')    






def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if username == 'mwema':
                messages.success(request, 'Authenticated Successfully, Now You Can Search')
                return redirect('/')
            elif user.is_cis_admin or user.is_superuser:
                return redirect('userboard')
            elif user.is_rms_officer:
                return redirect('dashboard')    
            else:
                return redirect('officer')                 
        else:
            messages.info(request,"Invalid username or password")
            return redirect('cis')    



def logout_view(request):
    logout(request)
    return redirect('cis')

@login_required
def update_file(request, pk):
    if request.method == 'POST':
        report = request.FILES['report']
        file_name = request.FILES['report'].name

        fs = FileSystemStorage()
        file = fs.save(report.name, report)
        fileurl = fs.url(file)
        fname = 'C:/Users/Public/motech/DJANGO/ma/media/' + file_name
        report = file_name


        Task.objects.filter(id = pk).update(report = report, status="completed")
        messages.success(request, 'Report was uploaded successfully!')
        return redirect('manage-tasks')
    else:
        return render(request, 'cis/dashboard/admin/de.html')


@login_required
def oupdate_file(request, pk):
    if request.method == 'POST':
        report = request.FILES['report']
        file_name = request.FILES['report'].name

        fs = FileSystemStorage()
        file = fs.save(report.name, report)
        fileurl = fs.url(file)
        fname = 'F:/PYCHARM/DJANGO/juaphe/media/' + file_name
        report = file_name


        Task.objects.filter(id = pk).update(report = report, status="completed")
        messages.success(request, 'Report was uploaded successfully!')
        return redirect('manage_caselist')
    else:
        return render(request, 'cis/dashboard/officer/de.html')



@login_required
def publish(request):
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


        a = Task(task_title=task_title, task_customer=task_customer, supervisor=supervisor, amount=amount, 
            task_desc=task_desc, task_deadline=task_deadline, status=status, created_at=created_at, task_days=task_days)
        a.save()
        messages.success(request, 'Case was added successfully!')
        return redirect('case_form')
    else:
        messages.error(request, 'Case was not added successfully!')
        return redirect('case_form')


@login_required
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


        a = Task(task_title=task_title, task_customer=task_customer, supervisor=supervisor, amount=amount, 
            task_desc=task_desc, task_deadline=task_deadline, report='', status=status, created_at=created_at, task_days=task_days)
        a.save()
        messages.success(request, 'Case was added successfully!')
        return redirect('addcase_form')
    else:
        messages.error(request, 'Case was not added successfully!')
        return redirect('addcase_form')
         

class UserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'cis/dashboard/admin/list_users.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        return User.objects.order_by('-id')


@login_required
def delete_task(request, pk):
    if request.method == 'POST':
        task = Task.objects.get(pk=pk)
        task.delete()
        messages.success(request, 'Data was deleted successfully!')
    return redirect('manage-tasks')


class CaseListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'cis/dashboard/officer/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10


    def get_queryset(self):
        return Task.objects.all()


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'cis/dashboard/admin/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10


    def get_queryset(self):
        return Task.objects.all()



class Pending(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'cis/dashboard/admin/pending.html'
    context_object_name = 'tasks'
    paginate_by = 10


    def get_queryset(self):
        return Task.objects.all().filter(status="pending")


class PenCase(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'cis/dashboard/officer/pending.html'
    context_object_name = 'tasks'
    paginate_by = 10


    def get_queryset(self):
        return Task.objects.all().filter(status="pending")


class UCreateChat(LoginRequiredMixin, CreateView):
    form_class = ChatForm
    model = Chat
    template_name = 'cis/dashboard/officer/chat_form.html'
    success_url = reverse_lazy('olchat')



    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ACreateChat(LoginRequiredMixin, CreateView):
    form_class = ChatForm
    model = Chat
    template_name = 'cis/dashboard/admin/chat_form.html'
    success_url = reverse_lazy('alchat')



    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class UListChat(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'cis/dashboard/officer/chat_list.html'
    paginate_by = 10


    def get_queryset(self):
        return Chat.objects.filter(posted_at__lt=timezone.now()).order_by('posted_at')


class ListUserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'cis/dashboard/admin/list_users.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        return User.objects.order_by('-id')
        

class AListChat(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'cis/dashboard/admin/chat_list.html'
    paginate_by = 10


    def get_queryset(self):
        return Chat.objects.filter(posted_at__lt=timezone.now()).order_by('posted_at')



class Completed(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'cis/dashboard/admin/completed.html'
    context_object_name = 'tasks'
    paginate_by = 10


    def get_queryset(self):
        return Task.objects.all().filter(status="completed")


class CompCase(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'cis/dashboard/officer/completed.html'
    context_object_name = 'tasks'
    paginate_by = 10


    def get_queryset(self):
        return Task.objects.all().filter(status="completed")





class SearchResults(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(task_title__icontains=query) | Q(task_desc__icontains=query)
        )
        return object_list


class UploadTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    template_name = 'cis/dashboard/admin/add_task.html'



@login_required   
def book_list(request):
    tasks = Task.objects.all()
    return render(request, 'cis/dashboard/admin/class_task_list.html', {
        'tasks': tasks
    })



class ManageTask(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'cis/dashboard/admin/manage_task.html'
    context_object_name = 'tasks'


class ManageTaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'cis/dashboard/officer/manage_task.html'
    context_object_name = 'tasks'



@login_required
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
			return render(request, "cis/dashboard/admin/change_quote.html",{"form": form})
	else:
		form = InspirationalQuoteForm()
		return render(request, "cis/dashboard/admin/change_quote.html",{"form": form})		


@login_required
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


class TaskView(LoginRequiredMixin, DetailView):
    model = Task


class DeleteTask(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'cis/dashboard/admin/confirm_delete.html'
    success_url = reverse_lazy('manage-tasks')
    success_message = "Data successfully deleted"


class UpdateTask(SuccessMessageMixin, UpdateView): 
    model = Task
    form_class = TaskForm
    template_name = 'cis/dashboard/admin/edit_task.html'
    success_url = reverse_lazy('manage-tasks')
    success_message = "Data successfully updated"



# User view
@login_required
def add_case(request):
    return render(request, 'cis/dashboard/user/add_case.html')

@login_required
def user_dashboard(request):
    return render(request, 'cis/dashboard/user/home.html')

@login_required
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


class UTaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'cis/dashboard/user/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 8

    def get_queryset(self):
        return Task.objects.all()



@login_required
def search(request):
    query = request.GET['q']
    print(type(query))
    print("Word T be searched", query)

    data = query.split()
    print(data)
    '-'.join(data)
    data = ' '.join(data)
    print(data)
    print(len(data))

    text = data
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()
    print(keyword_extracted)
    my_keyword = keyword_extracted
    '-'.join(my_keyword)
    print("Extracted Word By ML")
    print(' '.join(my_keyword))
    data = ' '.join(my_keyword)

    print("New Word According to ML", data)
    print(data)
    print("Before Again")

    if( len(data) == 0):
        return redirect('dashboard')
    else:
                print("Again")
                print(data)

                count = {}
                results = {}
                results['posts']= Task.objects.none() # empty QuerySet
                queries = data.split()
                print("my query below")
                print(queries)
                for query in queries:
                    results['posts'] = results['posts'] | Task.objects.filter(supervisor__icontains=query)
                    count['posts'] = results['posts'].count()


                count1 = {}
                queries1 = data.split()
                results1 = {}
                results1['posts']= Task.objects.none() # empty QuerySet
                queries1 = data.split()
                for query1 in queries:
                    results1['posts'] = results1['posts'] | Task.objects.filter(suspect__icontains=query1)
                    count1['posts'] = results1['posts'].count()

                count5 = {}
                queries5 = data.split()
                results5 = {}
                results5['posts'] = Task.objects.none()  # empty QuerySet
                queries5 = data.split()
                for query5 in queries:
                    results5['posts'] = results5['posts'] | Task.objects.filter(modus__icontains=query5)
                    count5['posts'] = results5['posts'].count()

                count2 = {}
                queries2 = data.split()
                results2 = {}
                results2['posts'] = Task.objects.none()  # empty QuerySet
                queries2 = data.split()
                for query2 in queries:
                    results2['posts'] = results2['posts'] | Task.objects.filter(task_title__icontains=query2)
                    count2['posts'] = results2['posts'].count()

                count3 = {}
                queries3 = data.split()
                results3 = {}
                results3['posts'] = Task.objects.none()  # empty QuerySet
                queries3 = data.split()
                for query3 in queries:
                    results3['posts'] = results3['posts'] | Task.objects.filter(task_customer__icontains=query3)
                    count3['posts'] = results3['posts'].count()

                count4 = {}
                queries4 = data.split()
                results4 = {}
                results4['posts'] = Task.objects.none()  # empty QuerySet
                queries4 = data.split()
                for query4 in queries:
                    results4['posts'] = results4['posts'] | Task.objects.filter(report__icontains=query4)
                    count4['posts'] = results4['posts'].count()

                count6 = {}
                queries6 = data.split()
                results6 = {}
                results6['posts'] = Task.objects.none()  # empty QuerySet
                queries6 = data.split()
                for query6 in queries:
                    results6['posts'] = results6['posts'] | Task.objects.filter(suspect__icontains=query4)
                    count6['posts'] = results6['posts'].count()

                count7 = {}
                queries7 = data.split()
                results7 = {}
                results7['posts'] = Task.objects.none()  # empty QuerySet
                queries7 = data.split()
                for query7 in queries:
                    results7['posts'] = results7['posts'] | Task.objects.filter(comment__icontains=query4)
                    count7['posts'] = results7['posts'].count()

                count8 = {}
                queries8 = data.split()
                results8 = {}
                results8['posts'] = Task.objects.none()  # empty QuerySet
                queries8 = data.split()
                for query8 in queries:
                    results8['posts'] = results8['posts'] | Task.objects.filter(status__icontains=query4)
                    count8['posts'] = results8['posts'].count()



                files = itertools.chain(results['posts'], results1['posts'], results2['posts'], results3['posts'], results4['posts'], results5['posts'], results6['posts'], results7['posts'], results8['posts'])

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
                    return render(request,'cis/dashboard/admin/result.html',{'files':files,'word':word})
                return render(request,'cis/dashboard/admin/result.html',{'files':files,'word':word})


@login_required
def osearch(request):
    query = request.GET['q']
    print(type(query))
    print("Word T be searched", query)

    data = query.split()
    print(data)
    '-'.join(data)
    data = ' '.join(data)
    print(data)
    print(len(data))

    text = data
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()
    print(keyword_extracted)
    my_keyword = keyword_extracted
    '-'.join(my_keyword)
    print("Extracted Word By ML")
    print(' '.join(my_keyword))
    data = ' '.join(my_keyword)

    print("New Word According to ML", data)
    print(data)
    print("Before Again")

    if( len(data) == 0):
        return redirect('officer')
    else:
                print("Again")
                print(data)

                count = {}
                results = {}
                results['posts']= Task.objects.none() # empty QuerySet
                queries = data.split()
                print("my query below")
                print(queries)
                for query in queries:
                    results['posts'] = results['posts'] | Task.objects.filter(supervisor__icontains=query)
                    count['posts'] = results['posts'].count()


                count1 = {}
                queries1 = data.split()
                results1 = {}
                results1['posts']= Task.objects.none() # empty QuerySet
                queries1 = data.split()
                for query1 in queries:
                    results1['posts'] = results1['posts'] | Task.objects.filter(suspect__icontains=query1)
                    count1['posts'] = results1['posts'].count()

                count5 = {}
                queries5 = data.split()
                results5 = {}
                results5['posts'] = Task.objects.none()  # empty QuerySet
                queries5 = data.split()
                for query5 in queries:
                    results5['posts'] = results5['posts'] | Task.objects.filter(modus__icontains=query5)
                    count5['posts'] = results5['posts'].count()

                count2 = {}
                queries2 = data.split()
                results2 = {}
                results2['posts'] = Task.objects.none()  # empty QuerySet
                queries2 = data.split()
                for query2 in queries:
                    results2['posts'] = results2['posts'] | Task.objects.filter(task_title__icontains=query2)
                    count2['posts'] = results2['posts'].count()

                count3 = {}
                queries3 = data.split()
                results3 = {}
                results3['posts'] = Task.objects.none()  # empty QuerySet
                queries3 = data.split()
                for query3 in queries:
                    results3['posts'] = results3['posts'] | Task.objects.filter(task_customer__icontains=query3)
                    count3['posts'] = results3['posts'].count()

                count4 = {}
                queries4 = data.split()
                results4 = {}
                results4['posts'] = Task.objects.none()  # empty QuerySet
                queries4 = data.split()
                for query4 in queries:
                    results4['posts'] = results4['posts'] | Task.objects.filter(report__icontains=query4)
                    count4['posts'] = results4['posts'].count()

                count6 = {}
                queries6 = data.split()
                results6 = {}
                results6['posts'] = Task.objects.none()  # empty QuerySet
                queries6 = data.split()
                for query6 in queries:
                    results6['posts'] = results6['posts'] | Task.objects.filter(suspect__icontains=query4)
                    count6['posts'] = results6['posts'].count()

                count7 = {}
                queries7 = data.split()
                results7 = {}
                results7['posts'] = Task.objects.none()  # empty QuerySet
                queries7 = data.split()
                for query7 in queries:
                    results7['posts'] = results7['posts'] | Task.objects.filter(comment__icontains=query4)
                    count7['posts'] = results7['posts'].count()

                count8 = {}
                queries8 = data.split()
                results8 = {}
                results8['posts'] = Task.objects.none()  # empty QuerySet
                queries8 = data.split()
                for query8 in queries:
                    results8['posts'] = results8['posts'] | Task.objects.filter(status__icontains=query4)
                    count8['posts'] = results8['posts'].count()



                files = itertools.chain(results['posts'], results1['posts'], results2['posts'], results3['posts'], results4['posts'], results5['posts'], results6['posts'], results7['posts'], results8['posts'])

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
                    return render(request,'cis/dashboard/officer/result.html',{'files':files,'word':word})
                return render(request,'cis/dashboard/officer/result.html',{'files':files,'word':word})
