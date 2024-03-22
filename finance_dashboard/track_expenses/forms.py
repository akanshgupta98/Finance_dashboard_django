from django import forms
from django.forms import ModelForm
from .models import Expense


class SignUpForm(forms.Form):

    firstName = forms.CharField(required=False)
    lastName = forms.CharField(required=False)
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    confirmPassword = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class TrackExpenseModelForm(ModelForm):
    user = forms.CharField(required=False)
    new_category = forms.CharField(required=False)
    class Meta:
        model = Expense
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        print('celaned data is: ',cleaned_data)
        category = cleaned_data.get('expenseCategory')
        new_category = cleaned_data.get('new_category')
        
        if category == 'Other' and new_category:
            cleaned_data['expenseCategory'] = new_category
            new_choices = []
            new_choices = list(self.fields['expenseCategory'].choices)
            print('new chocies ',new_choices)

            new_choices.append((new_category.capitalize(),new_category))
            print('new choices are: ',new_choices)
            self.fields['expenseCategory'].choices = new_choices
        
        return cleaned_data

    