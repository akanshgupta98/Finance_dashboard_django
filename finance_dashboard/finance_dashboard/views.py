from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import render,redirect
from track_expenses.forms import (
    SignUpForm,
    LoginForm,
    TrackExpenseModelForm,
)
from track_expenses.models import Expense
import datetime

from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth.decorators import login_required

def home_page(request):

    return render(request,"home.html")

@login_required
def logout_page(request):
    logout(request)
    return redirect("/")

# def login_page(request):
#     loginForm = LoginForm(request.POST or None)

#     if loginForm.is_valid():
#         loginFormData = {
#             "username" : loginForm.cleaned_data['username'],
#             "password" : loginForm.cleaned_data['password']
#         }

#         authenticated_user = authenticate(request,**loginFormData)
#         if authenticated_user is not None:
#             login(request,authenticated_user)
#             return redirect("/")
        
#         else:
#             print("LOGIN FAILED")
    
#     context = {"login_form":loginForm}
        
        

#     return render(request,"login.html",context)

def about_page(request):
    return render(request,"about.html")

@login_required(login_url="/login/")
def track_page(request):

    expenseForm = TrackExpenseModelForm(request.POST or None)
    # expenseForm.fields.expenseCategory.CATEGORY_IN_EXPENSE_CHOICES['new'] = 'New'
    # print('fields: ',expenseForm)

    # context = {"choices":expenseForm.CATEGORY_IN_EXPENSE_CHOICES}

    if expenseForm.is_valid():
        expenses = expenseForm.save(commit=False)
        expenses.user = request.user
        
        expenses.save()
    
    else:
        print(expenseForm.errors)
    
    # print('FORM CATEGORY',expenseForm.expenseCategory)
        


    return render(request,"track.html",{'form': expenseForm})

def signup_page(request):
    signupForm = SignUpForm(request.POST or None)

    if signupForm.is_valid():
        userFormData = {
            
            "username" : signupForm.cleaned_data['username'],
            "email" : signupForm.cleaned_data['email'],
            "password" : signupForm.cleaned_data['password'],
            
        }

        # userFormData = **signupForm.cleaned_data
        print("USER FORM DATA",userFormData)
        user = User.objects.create_user(**userFormData)
        
        if signupForm.cleaned_data['firstName'] != "":
            user.first_name = signupForm.cleaned_data['firstName']
        if signupForm.cleaned_data['lastName'] != "":
            user.last_name = signupForm.cleaned_data['lastName']
        
        
        user.save()
        return redirect("/login/")
    else:
        print(signupForm.errors)

    return render(request,"signup.html")

def profile_page(request):
    return render(request,"profile.html")

# @login_required('/login/')
def expenses_page(request):
    print("REQUEST IS",request)
    current_month = timezone.now().month
    current_year = timezone.now().year

    qs = Expense.objects.filter(
        Q(expenseDate__month=current_month, expenseDate__year=current_year) & Q(user=request.user)
    )
    monthly_expense = 0
    for expense in qs:
        monthly_expense += expense.expenseAmount
    context = {"object":qs,"monthly_expense":monthly_expense}
    print(qs.first().expenseDate.strftime("%b"))
    return render(request,"view_expenses.html",context)

def visual_trends_page(request):
    return render(request,"visualize_trends.html")