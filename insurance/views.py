from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.core import serializers
from django.conf import settings
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from datetime import datetime, date
from django.core.exceptions import ValidationError
from . import models
import operator
import itertools
from django.db.models import Avg, Count, Sum
from django.forms import inlineformset_factory
#from .models import TakenQuiz
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm)

from django.contrib.auth import update_session_auth_hash                                       

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

import pandas as pd
from django.http import JsonResponse
from django.http import HttpResponse
from pandas import read_csv
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import joblib as joblib
import argparse
import os
import sklearn
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer



def home_two(request):
  return render(request, 'bonge/home.html')


def home(request):
  genders = {'male':1, 'female':0}
  injurys = {'bad':1, 'normal':0} 
  return render(request, 'bonge/home.html', genders)


def alliance(request):
   if request.method == 'POST':
     user_input = request.POST['data']

     dataset = os.path.join('F:/PYCHARM/DJANGO/insurance/data', 'dataset.csv')
     dataset = read_csv(dataset)

     # Feature selection
     df = dataset[['content','class']]
     df_x = df['content']
     df_y = df['class']


     corpus = df_x
     vectorizer = CountVectorizer()
     X = vectorizer.fit_transform(corpus)

     # Train Test Split
     X_train, X_test, y_train, y_test = train_test_split(X,df_y, test_size=0.3, random_state=42)


     # Fit the Model
     clf = MultinomialNB()
     clf.fit(X_train, y_train)
     clf.score(X_test, y_test)


     data = [user_input]
     print(data)
     vect = vectorizer.transform(data).toarray()
     print(type(vect))
     my_prediction = clf.predict(vect)
     my_prediction = my_prediction[0]
     print(my_prediction)

     messages.success(request, my_prediction)
     return redirect('home_two')
   else:
     return render(request, 'bonge/home2.html')
     


def insurance(request):
  if request.method == 'POST':
    gender = request.POST['gender']
    gender = int(gender)
    marital = request.POST['marital']
    marital = int(marital)
    licence = request.POST['licence']
    licence = int(licence)
    injury = request.POST['injury']
    injury = int(injury)
    police = request.POST['police']
    police = int(police)
    day = request.POST['day']
    day = int(day)
    witness = request.POST['witness']
    witness = int(witness)
    amount = request.POST['amount']
    amount = int(amount)
    age = request.POST['age']
    age = int(age)


    data = [gender,marital,licence,injury,police,day,age,witness,amount]
    x = np.array(data).reshape(1,-1)
    x = np.array(x, dtype=np.int64)


    # Loading the model
    model = os.path.join('F:/PYCHARM/DJANGO/insurance/model', 'forest.pkl')
    model = joblib.load(model)

    result = model.predict(x)
    print(result[0])
    result = result[0]
    if result == 1:
      print("The Claim is False")
      messages.success(request, 'The Claim is Fraud')
      return redirect('insurance')
    elif result == 0:
      print("The Calim is True")
      messages.success(request, 'The Claim is Ok')
      return redirect('insurance')
    else:
      return redirect('insurance')
  else:
      print("Please Try Again")
      return redirect('insurance')


def predictdisease(request):
    if request.method == 'POST':
        Symptom1 = request.POST["Symptom1"]
        Symptom2 = request.POST["Symptom2"]
        Symptom3 = request.POST["Symptom3"]
        Symptom4 = request.POST["Symptom4"]
        Symptom5 = request.POST["Symptom5"]

    psymptoms = [Symptom1, Symptom2, Symptom3, Symptom4, Symptom5]
    print("Received Input From User")
    print(psymptoms)

    # Training dataset
    data = pd.read_csv(os.path.join('D:/PYCHARM/DJANGO/ujasi/bonge/dataset', 'Training.csv'))
    print(len(data))
    
    return HttpResponse("I will give prediction soon")


def team(request):
    return render(request, 'bonge/team.html')


def hey(request):
    return render(request, 'bonge/hey.html')


def predict(request):
    return render(request, 'bonge/result.html')



def handler404(request, exception):
  return render(request, 'bonge/404.html')

def about(request):
  return render(request, 'bonge/about.html')