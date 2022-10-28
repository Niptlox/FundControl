from django import forms
from django.forms import ModelForm

from main.models import Expense


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"
