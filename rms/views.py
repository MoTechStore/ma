from django.shortcuts import render
from rms.models import Store, Letter, Letters, File
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from . import models
import operator
import itertools
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CustomerForm, UserForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from cis.models import Task
from insurance.models import Insurancefile
from kye.models import Employee, Company
from rms.models import File,Letter,Letters


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
import pandas as pd
import string
import os
import fitz

from django.conf import settings



from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)


from rake_nltk import Rake
rake_nltk_var = Rake()



@login_required
def ai_search(request):
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
        return redirect('ma')
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
                    results['posts'] = results['posts'] | Task.objects.filter(task_title__icontains=query)
                    count['posts'] = results['posts'].count()



                count2 = {}
                queries2 = data.split()
                results2 = {}
                results2['posts'] = Task.objects.none()  # empty QuerySet
                queries2 = data.split()
                for query2 in queries:
                    results2['posts'] = results2['posts'] | Task.objects.filter(task_desc__icontains=query2)
                    count2['posts'] = results2['posts'].count()



                count5 = {}
                queries5 = data.split()
                results5 = {}
                results5['posts'] = Insurancefile.objects.none()  # empty QuerySet
                queries5 = data.split()
                for query5 in queries:
                    results5['posts'] = results5['posts'] | Insurancefile.objects.filter(insurer__icontains=query5)
                    count5['posts'] = results5['posts'].count()


                count6 = {}
                queries6 = data.split()
                results6 = {}
                results6['posts'] = Insurancefile.objects.none()  # empty QuerySet
                queries6 = data.split()
                for query6 in queries:
                    results6['posts'] = results6['posts'] | Insurancefile.objects.filter(claimant__icontains=query6)
                    count6['posts'] = results6['posts'].count()

                count7 = {}
                queries7 = data.split()
                results7 = {}
                results7['posts'] = Insurancefile.objects.none()  # empty QuerySet
                queries7 = data.split()
                for query7 in queries:
                    results7['posts'] = results7['posts'] | Insurancefile.objects.filter(deceased__icontains=query7)
                    count7['posts'] = results7['posts'].count()

                count8 = {}
                queries8 = data.split()
                results8 = {}
                results8['posts'] = Insurancefile.objects.none()  # empty QuerySet
                queries8 = data.split()
                for query8 in queries:
                    results8['posts'] = results8['posts'] | Insurancefile.objects.filter(driver__icontains=query8)
                    count8['posts'] = results8['posts'].count()


                count9 = {}
                queries9 = data.split()
                results9 = {}
                results9['posts'] = Employee.objects.none()  # empty QuerySet
                queries9 = data.split()
                for query9 in queries:
                    results9['posts'] = results9['posts'] | Employee.objects.filter(firstname__icontains=query9)
                    count9['posts'] = results9['posts'].count()


                count10 = {}
                queries10 = data.split()
                results10 = {}
                results10['posts'] = Employee.objects.none()  # empty QuerySet
                queries10 = data.split()
                for query10 in queries:
                    results10['posts'] = results10['posts'] | Employee.objects.filter(middlename__icontains=query10)
                    count8['posts'] = results10['posts'].count()



                count11 = {}
                queries11 = data.split()
                results11 = {}
                results11['posts'] = Employee.objects.none()  # empty QuerySet
                queries11 = data.split()
                for query11 in queries:
                    results11['posts'] = results11['posts'] | Employee.objects.filter(lastname__icontains=query11)
                    count11['posts'] = results11['posts'].count()



                count15 = {}
                queries15 = data.split()
                results15 = {}
                results15['posts']= Task.objects.none() # empty QuerySet
                queries15 = data.split()
                for query15 in queries:
                    results15['posts'] = results15['posts'] | Task.objects.filter(task_desc__icontains=query15)
                    count15['posts'] = results15['posts'].count()

                count13 = {}
                queries13 = data.split()
                results13 = {}
                results13['posts'] = Letter.objects.none()  # empty QuerySet
                queries13 = data.split()
                for query13 in queries:
                    results13['posts'] = results13['posts'] | Letter.objects.filter(sender__icontains=query13)
                    count13['posts'] = results13['posts'].count()

                count16 = {}
                queries16 = data.split()
                results16 = {}
                results16['posts'] = Letter.objects.none()  # empty QuerySet
                queries16 = data.split()
                for query16 in queries:
                    results16['posts'] = results16['posts'] | Letter.objects.filter(desc__icontains=query16)
                    count16['posts'] = results16['posts'].count()

                count17 = {}
                queries17 = data.split()
                results17 = {}
                results17['posts'] = Letters.objects.none()  # empty QuerySet
                queries17 = data.split()
                for query17 in queries:
                    results17['posts'] = results17['posts'] | Letters.objects.filter(receiver_name__icontains=query17)
                    count17['posts'] = results17['posts'].count()

                count18 = {}
                queries18 = data.split()
                results18 = {}
                results18['posts'] = Letters.objects.none()  # empty QuerySet
                queries18 = data.split()
                for query18 in queries:
                    results18['posts'] = results18['posts'] | Letters.objects.filter(desc_two__icontains=query18)
                    count18['posts'] = results18['posts'].count()






                files = itertools.chain(results['posts'], results18['posts'], results17['posts'], results16['posts'], results13['posts'], results5['posts'], results6['posts'], results7['posts'], results8['posts'], results9['posts'], results10['posts'], results11['posts'], results15['posts'])

                res = []
                for i in files:
                    if i not in res:
                        res.append(i)

                # word variable will be shown in html when user click on search button
                word="Searched Result :"

                print(res)
                print(type(res))
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
                    return render(request,'rms/result.html',{'files':files,'word':word})
                return render(request,'rms/result.html',{'files':files,'word':word})









class LIcomingLetter(LoginRequiredMixin, ListView):
    model = Letter
    template_name = 'dashboard/admin/list_incoming_letter.html'
    context_object_name = 'letters'



class LOutgoingLetter(LoginRequiredMixin, ListView):
    model = Letters
    template_name = 'dashboard/admin/list_outgoing_letter.html'
    context_object_name = 'letters'




def ma(request):
    return render(request, 'rms/ma.html')


def usearch(request):
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
                results['posts']= File.objects.none() # empty QuerySet
                queries = data.split()
                print("my query below")
                print(queries)
                for query in queries:
                    results['posts'] = results['posts'] | File.objects.filter(file_name__icontains=query)
                    count['posts'] = results['posts'].count()


                count1 = {}
                queries1 = data.split()
                results1 = {}
                results1['posts']= File.objects.none() # empty QuerySet
                queries1 = data.split()
                for query1 in queries:
                    results1['posts'] = results1['posts'] | File.objects.filter(about_file__icontains=query1)
                    count1['posts'] = results1['posts'].count()

                count5 = {}
                queries5 = data.split()
                results5 = {}
                results5['posts'] = File.objects.none()  # empty QuerySet
                queries5 = data.split()
                for query5 in queries:
                    results5['posts'] = results5['posts'] | File.objects.filter(keyword__icontains=query5)
                    count5['posts'] = results5['posts'].count()

                count2 = {}
                queries2 = data.split()
                results2 = {}
                results2['posts'] = File.objects.none()  # empty QuerySet
                queries2 = data.split()
                for query2 in queries:
                    results2['posts'] = results2['posts'] | File.objects.filter(ref_number__icontains=query2)
                    count2['posts'] = results2['posts'].count()

                count3 = {}
                queries3 = data.split()
                results3 = {}
                results3['posts'] = File.objects.none()  # empty QuerySet
                queries3 = data.split()
                for query3 in queries:
                    results3['posts'] = results3['posts'] | File.objects.filter(keyword__icontains=query3)
                    count3['posts'] = results3['posts'].count()  


                files = itertools.chain(results['posts'], results1['posts'], results2['posts'], results3['posts'])

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
                    return render(request,'crow/result.html',{'files':files,'word':word})
                return render(request,'crow/result.html',{'files':files,'word':word})









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
                results['posts']= File.objects.none() # empty QuerySet
                queries = data.split()
                print("my query below")
                print(queries)
                for query in queries:
                    results['posts'] = results['posts'] | File.objects.filter(file_name__icontains=query)
                    count['posts'] = results['posts'].count()


                count1 = {}
                queries1 = data.split()
                results1 = {}
                results1['posts']= File.objects.none() # empty QuerySet
                queries1 = data.split()
                for query1 in queries:
                    results1['posts'] = results1['posts'] | File.objects.filter(about_file__icontains=query1)
                    count1['posts'] = results1['posts'].count()

                count5 = {}
                queries5 = data.split()
                results5 = {}
                results5['posts'] = File.objects.none()  # empty QuerySet
                queries5 = data.split()
                for query5 in queries:
                    results5['posts'] = results5['posts'] | File.objects.filter(keyword__icontains=query5)
                    count5['posts'] = results5['posts'].count()

                count2 = {}
                queries2 = data.split()
                results2 = {}
                results2['posts'] = File.objects.none()  # empty QuerySet
                queries2 = data.split()
                for query2 in queries:
                    results2['posts'] = results2['posts'] | File.objects.filter(ref_number__icontains=query2)
                    count2['posts'] = results2['posts'].count()

                count3 = {}
                queries3 = data.split()
                results3 = {}
                results3['posts'] = File.objects.none()  # empty QuerySet
                queries3 = data.split()
                for query3 in queries:
                    results3['posts'] = results3['posts'] | File.objects.filter(keyword__icontains=query3)
                    count3['posts'] = results3['posts'].count()  


                files = itertools.chain(results['posts'], results1['posts'], results2['posts'], results3['posts'])

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



def search_letter(request):
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
                results['posts']= Letter.objects.none() # empty QuerySet
                queries = data.split()
                print("my query below")
                print(queries)
                for query in queries:
                    results['posts'] = results['posts'] | Letter.objects.filter(ref_number__icontains=query)
                    count['posts'] = results['posts'].count()


                count1 = {}
                queries1 = data.split()
                results1 = {}
                results1['posts']= Letter.objects.none() # empty QuerySet
                queries1 = data.split()
                for query1 in queries:
                    results1['posts'] = results1['posts'] | Letter.objects.filter(desc__icontains=query1)
                    count1['posts'] = results1['posts'].count()

                

                count2 = {}
                queries2 = data.split()
                results2 = {}
                results2['posts'] = Letter.objects.none()  # empty QuerySet
                queries2 = data.split()
                for query2 in queries:
                    results2['posts'] = results2['posts'] | Letter.objects.filter(sender__icontains=query2)
                    count2['posts'] = results2['posts'].count()

                count3 = {}
                queries3 = data.split()
                results3 = {}
                results3['posts'] = Letter.objects.none()  # empty QuerySet
                queries3 = data.split()
                for query3 in queries:
                    results3['posts'] = results3['posts'] | Letter.objects.filter(date__icontains=query3)
                    count3['posts'] = results3['posts'].count()


                count4 = {}
                queries4 = data.split()
                results4 = {}
                results4['posts'] = Letter.objects.none()  # empty QuerySet
                queries4 = data.split()
                for query4 in queries:
                    results4['posts'] = results4['posts'] | Letter.objects.filter(receiver__icontains=query4)
                    count4['posts'] = results4['posts'].count()


                count5 = {}
                queries5 = data.split()
                results5 = {}
                results5['posts'] = Letters.objects.none()  # empty QuerySet
                queries5 = data.split()
                for query5 in queries:
                    results5['posts'] = results5['posts'] | Letters.objects.filter(sender_name__icontains=query5)
                    count5['posts'] = results5['posts'].count()    
                    


                count6 = {}
                queries6 = data.split()
                results6 = {}
                results6['posts'] = Letters.objects.none()  # empty QuerySet
                queries6 = data.split()
                for query6 in queries:
                    results6['posts'] = results6['posts'] | Letters.objects.filter(receiver_address__icontains=query3)
                    count6['posts'] = results6['posts'].count()
                    

                count7 = {}
                queries7 = data.split()
                results7 = {}
                results7['posts'] = Letters.objects.none()  # empty QuerySet
                queries7 = data.split()
                for query7 in queries:
                    results7['posts'] = results7['posts'] | Letters.objects.filter(receiver_name__icontains=query3)
                    count7['posts'] = results7['posts'].count()
                    


                count8 = {}
                queries8 = data.split()
                results8 = {}
                results8['posts'] = Letters.objects.none()  # empty QuerySet
                queries8 = data.split()
                for query8 in queries:
                    results8['posts'] = results8['posts'] | Letters.objects.filter(ref_number_two__icontains=query3)
                    count8['posts'] = results8['posts'].count()



                count9 = {}
                queries9 = data.split()
                results9 = {}
                results9['posts'] = Letters.objects.none()  # empty QuerySet
                queries9 = data.split()
                for query9 in queries:
                    results9['posts'] = results9['posts'] | Letters.objects.filter(date_two__icontains=query3)
                    count9['posts'] = results9['posts'].count() 
                    

                count10 = {}
                queries10 = data.split()
                results10 = {}
                results10['posts'] = Letters.objects.none()  # empty QuerySet
                queries10 = data.split()
                for query10 in queries:
                    results10['posts'] = results10['posts'] | Letters.objects.filter(desc_two__icontains=query3)
                    count10['posts'] = results10['posts'].count()                           


                files = itertools.chain(results['posts'], results1['posts'], results2['posts'], results3['posts'], results4['posts'], results5['posts'], results6['posts'], results7['posts'], results8['posts'], results9['posts'], results10['posts'])

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
                    return render(request,'dashboard/admin/letter_result.html',{'files':files,'word':word})
                return render(request,'dashboard/admin/letter_result.html',{'files':files,'word':word})



class AListTruckReadView(BSModalReadView):
    model = User
    template_name = 'dashboard/admin/r_admin_truck.html'



class UserView(generic.ListView):
    model = User
    template_name = 'dashboard/admin/list_users.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        return User.objects.order_by('-id')

class AdminListReadView(BSModalReadView):
    model = Store
    template_name = 'dashboard/admin/r_admin_list.html'


def update_file(request, pk):
    if request.method == 'POST':
        report = request.FILES['report']
        file_name = request.FILES['report'].name

        fs = FileSystemStorage()
        file = fs.save(report.name, report)
        fileurl = fs.url(file)
        report = file_name


        Store.objects.filter(id = pk).update(file = report)
        messages.success(request, 'Report was uploaded successfully!')
        return redirect('manage-files')
    else:
        messages.error(request, 'Report was not uploaded successfully')
        return redirect('manage-files')

class AlUpdateView(BSModalUpdateView):
    model = Store
    template_name = 'dashboard/admin/al_update.html'
    form_class = CustomerForm
    success_message = 'Success: Data was updated.'
    success_url = reverse_lazy('manage_files')


class UserUpdateView(BSModalUpdateView):
    model = User
    template_name = 'dashboard/admin/u_update.html'
    form_class = UserForm
    success_message = 'Success: Data was updated.'
    success_url = reverse_lazy('users')




class ListItDeleteView(BSModalDeleteView):
    model = Store
    template_name = 'dashboard/admin/admin_list_delete.html'
    success_message = 'Success: Data was deleted.'
    success_url = reverse_lazy('manage_files')



class DeleteUserView(BSModalDeleteView):
    model = User
    template_name = 'dashboard/admin/delete_user.html'
    success_message = 'Success: Data was deleted.'
    success_url = reverse_lazy('users')


def home(request):
    return render(request, 'dashboard/admin/home.html')


def signup(request):
    return render(request, 'dashboard/admin/home.html')


def dashboard(request):
    return render(request, 'dashboard/admin/home.html')


def add_file(request):
    return render(request, 'dashboard/admin/add_file.html')


def add_letter(request):
    return render(request, 'dashboard/admin/add_letter.html')


def out_letter(request):
    return render(request, 'dashboard/admin/out_letter.html')

def index(request):
    return render(request, 'crow/index.html')


def test(request):
    return render(request, 'crow/test.html')

from django.core.files.storage import FileSystemStorage

def cv_insight(request):
    if request.method == 'POST':
        report = request.FILES['report']
        file_name = request.FILES['report'].name

        print(file_name)


        fs = FileSystemStorage()
        file = fs.save(report.name, report)
        print(file)

        report = 'C:/Users/Public/motech/DJANGO/ma/media/' + file
        print('CV processed', report)

        
        data = pd.read_csv(os.path.join('C:/Users/MoTech/Desktop/AI/CV/MWEMA', 'clean.csv'))

        report = open(os.path.join(settings.MEDIA_ROOT, report))
        # Feature selection
        df_x = data['posts']
        df_y = data['type']

        tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin_1', ngram_range=(1,2), stop_words='english')
        x_train, x_test, y_train, y_test = train_test_split(data['posts'], data['type'], random_state=0, train_size=0.7, test_size=0.3)
        count_vectorizer = CountVectorizer()
        x_train_occurences = count_vectorizer.fit_transform(x_train)
        tfidf_transformer = TfidfTransformer()
        x_tfidf = tfidf_transformer.fit_transform(x_train_occurences)

        # Fit The Model
        model = LinearSVC()
        model.fit(x_tfidf, y_train)
        model.score(x_tfidf, y_train)
        model_acc = model.score(x_tfidf, y_train)
        print(model_acc)
        print('Hi MoTech')

        with fitz.open(report) as doc:
            text = ""
            for page in doc:
                text += page.getText()

        data = text
        prediction = model.predict(count_vectorizer.transform([data])[0])
        prediction = prediction[0]
        print(prediction)
        context = {'prediction': prediction}
        return render(request, 'rms/cv.html', context)
    else:    
        return render(request, 'rms/cv.html')



class ManageFileView(ListView):
    model = File
    template_name = 'dashboard/admin/manage_file.html'
    context_object_name = 'stores'
    paginate_by = 7


    def get_queryset(self):
        return File.objects.order_by('-id')


def logout_view(request):
    logout(request)
    return redirect('ma')


    sender = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    receiver = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    date = models.DateTimeField(blank=True, null=True)


def save_letter(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        address =  request.POST['address']
        receiver = request.POST['receiver']
        contact = request.POST['contact']
        desc = request.POST['desc']
        date = request.POST['date']
        ref_number = request.POST['ref_number']


        a = Letter(sender=sender, address=address, receiver=receiver, contact=contact, desc=desc, date=date, ref_number=ref_number)
        a.save()
        messages.success(request, "Incoming Letter Added successfully")
        return redirect('addletter')





def outing_letter(request):
    if request.method == 'POST':
        sender_name = request.POST['sender_name']
        receiver_address =  request.POST['receiver_address']
        receiver_name = request.POST['receiver_name']
        contact = request.POST['contact']
        desc = request.POST['desc']
        date = request.POST['date']
        date = request.POST['date']
        ref_number = request.POST['ref_number']




        a = Letters(sender_name=sender_name, receiver_address=receiver_address, receiver_name=receiver_name, desc_two=desc, date_two=date, contact_two=contact, ref_number_two=ref_number)
        a.save()
        messages.success(request, "Outgoing Letter Added successfully")
        return redirect('outletter')






def save_file(request):
    if request.method == 'POST':
        file_name = request.POST['file_name']
        file_number = request.POST['file_number']
        cupboard_name = request.POST['cupboard_name']
        cupboard_number = request.POST['cupboard_number']
        shelve_number = request.POST['shelve_number']
        about_file = request.POST['about_document']
        ref_number = request.POST['ref_number']
        keyword = request.POST['name_list']

        a = File(file_name=file_name, file_number=file_number, cupboard_name=cupboard_name, cupboard_number=cupboard_number,
            shelve_number=shelve_number, about_file=about_file, ref_number=ref_number)
        a.save()

        messages.success(request, "File Added successfully")
        return redirect('addfile')



def save_data(request):
    if request.method == 'POST':
    	document_name = request.POST['document_name']
    	document_number =  request.POST['document_number']
    	file_name = request.POST['file_name']
    	file_number = request.POST['file_number']
    	cupboard_name = request.POST['cupboard_name']
    	cupboard_number = request.POST['cupboard_number']
    	shelve_number = request.POST['shelve_number']
    	about_document = request.POST['about_document']
    	ref_number = request.POST['ref_number']
    	name_list = request.POST['name_list']

    	a = Store(document_name=document_name, document_number=document_number, file_name=file_name,
        	file_number=file_number, cupboard_name=cupboard_name, cupboard_number=cupboard_number,
        	shelve_number=shelve_number, about_document=about_document, ref_number=ref_number,
        	name_list=name_list, accessed_no=0)
    	a.save()

    return HttpResponseRedirect(reverse('addfile'))



class FileListView(ListView):
    model = File
    template_name = 'dashboard/admin/recent_added_files.html'
    context_object_name = 'stores'


def search_view(request):
    query = request.GET['query']
    print(type(query))



    data = query.split()
    print(len(data))
    if( len(data) != 3):
        return redirect('index')
    else:
                a = data[0]
                print(a)
                b= data[1]
                print(b)
                c = data[2]
                print(c)


                # First word
                qs1 =models.Store.objects.all().filter(document_name__contains=a)
                qs2 =models.Store.objects.select_related().filter(document_name__contains=a).distinct()
                qs3 =models.Store.objects.filter(document_name__startswith=a).distinct()
                qs4 =models.Store.objects.filter(document_name__endswith=a).distinct()
                qs5 =models.Store.objects.filter(document_name__istartswith=a).distinct()
                qs6 =models.Store.objects.all().filter(document_name__icontains=a)
                qs7 =models.Store.objects.filter(document_name__iendswith=a).distinct()
                qs8 =models.Store.objects.filter(document_name__iexact=a).distinct()

                # Second word
                qs9 =models.Store.objects.all().filter(about_document__contains=b)
                qs10 =models.Store.objects.select_related().filter(about_document__contains=b).distinct()
                qs11 =models.Store.objects.filter(about_document__startswith=b).distinct()
                qs12 =models.Store.objects.filter(about_document__endswith=b).distinct()
                qs13 =models.Store.objects.filter(about_document__istartswith=b).distinct()
                qs14 =models.Store.objects.all().filter(about_document__icontains=b)
                qs15 =models.Store.objects.filter(about_document__iendswith=b).distinct()
                qs16 =models.Store.objects.filter(about_document__iexact=b).distinct()

                # Third word
                qs17 =models.Store.objects.all().filter(name_list__contains=c)
                qs18 =models.Store.objects.select_related().filter(name_list__contains=c).distinct()
                qs19 =models.Store.objects.filter(name_list__startswith=c).distinct()
                qs20 =models.Store.objects.filter(name_list__endswith=c).distinct()
                qs21 =models.Store.objects.filter(name_list__istartswith=c).distinct()
                qs22 =models.Store.objects.all().filter(name_list__icontains=c)
                qs23 =models.Store.objects.filter(name_list__iendswith=c).distinct()
                qs24 =models.Store.objects.filter(name_list__iexact=c).distinct()

                files = itertools.chain(qs1, qs2, qs3, qs4, qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13, qs14, qs15, qs16, qs17, qs18, qs19, qs20, qs21, qs22, qs23, qs24)

                res = []
                for i in files:
                    if i not in res:
                        res.append(i)


                # word variable will be shown in html when user click on search button
                word="Searched Result :"

                print(res)
                files = res


                """
                paginator = Paginator(posts_list, 6) # 6 posts per page
                page = request.GET.get('page')

                """


                page = request.GET.get('page', 1)
                paginator = Paginator(files, 10)
                try:
                    files = paginator.page(page)
                except PageNotAnInteger:
                    files = paginator.page(1)
                except EmptyPage:
                    files = paginator.page(paginator.num_pages)
   




                if files:
                    return render(request,'crow/result.html',{'files':files,'word':word})
                return render(request,'crow/result.html',{'files':files,'word':word})



from django.db.models.functions import Cast


class crudAdmin():
    def found(request, pk):
        #Truck.objects.filter(id = pk).update(is_payed = "True")
        #accessed_no = Store.objects.values_list('accessed_no').filter( id = pk)
        accessed_no = Store.objects.filter( id = pk).values_list('accessed_no', flat=True)[0]
        print(accessed_no)
        print(type(accessed_no))

        accessed_no = accessed_no + 1
        Store.objects.filter(id = pk).update(accessed_no = accessed_no)            
        return HttpResponseRedirect(reverse('manage_files'))