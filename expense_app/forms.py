from django import forms

from expense_app.models import Expense


# Form class for Expense Model
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'cost', 'description']
