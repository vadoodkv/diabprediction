from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from diabapp.models import signup
from django.http import JsonResponse

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def homepg(request):
    return render (request,'home.html')

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        myuser=authenticate(username=username,password=password)
        
        if myuser is not None:
            login(request, myuser)
            return redirect('pred')

        else:
            return render(request, 'signin.html', {'error': 'Invalid username or password'})
        
        
    return render(request,'signin.html')

def signups(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        address=request.POST['address']
        dob=request.POST['dob']
        phone=request.POST['phone']
        password=request.POST['password']
        
        if User.objects.filter(username=username).exists():
            
            return render(request, 'signup.html', {'error': 'Username already exists'})
        
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        
        signup_obj=signup(username=username,email=email,address=address,dob=dob,phone=phone)
        signup_obj.save()
        
        return redirect('sin')
        
    return render (request,'signup.html')

def predict(request):
   
    return render(request,'predict.html')




def result(request):
    data = pd.read_csv(r"diabetes.csv")
    
    x = data.drop('Outcome',axis=1)
    y = data['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30)
    
    model = LogisticRegression(max_iter=500)
    model.fit(X_train,y_train)
    
    val1=float(request.GET['n1'])
    val2=float(request.GET['n2'])
    val3=float(request.GET['n3'])
    val4=float(request.GET['n4'])
    val5=float(request.GET['n5'])
    val6=float(request.GET['n6'])
    val7=float(request.GET['n7'])
    val8=float(request.GET['n8'])
    
    pred=model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    
    result1="" 
    if pred==[1]:
        result1="POSITIVE"
    else:
        result1="NEGATIVE"
        
    
    return render(request,'predict.html',{"result2":result1})



