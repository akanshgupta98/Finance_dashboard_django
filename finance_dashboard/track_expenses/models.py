from django.db import models
from django.conf import settings
import datetime

User = settings.AUTH_USER_MODEL

# Create your models here.

class Expense(models.Model):

    FOOD = "Food"
    TRANSPORT = "Transport"
    UTILITY = "Utilities"
    INVESTMENT = "Investment"
    OTHER_CHOICE = "Other"
    CATEGORY_IN_EXPENSE_CHOICES = [
        (FOOD, "Food"),
        (TRANSPORT, "Transport"),
        (INVESTMENT, "Investment"),
        (UTILITY, "Utilities"),
        (OTHER_CHOICE, "Other"),
        
    ]
    
    user            = models.ForeignKey(User,on_delete = models.CASCADE,default=1)
    expenseName     = models.TextField()
    expenseAmount   = models.IntegerField()
    expenseCategory = models.TextField(choices = CATEGORY_IN_EXPENSE_CHOICES)
    expenseDate     = models.DateField()

'''TO DO: IMPLEMENT DYNAMIC CATEGORY ADDITION'''
# class Categories(models.Model):
#     user = models.ForeignKey(User,on_delete = models.CASCADE,default=1)
#     category = models.TextField(unique = True, default = "Other")
