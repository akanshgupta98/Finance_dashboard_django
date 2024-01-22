from django.db import models

# Create your models here.

class Expense(models.Model):
    FOOD = "Food"
    TRANSPORT = "Transport"
    CAR = "Car"
    CATEGORY_IN_EXPENSE_CHOICES = {
        FOOD: "Food",
        TRANSPORT: "Transport",
        CAR: "Car",
    }
    expenseName = models.TextField()
    expenseAmount = models.IntegerField()
    expenseCategory = models.TextField(choices = CATEGORY_IN_EXPENSE_CHOICES)
