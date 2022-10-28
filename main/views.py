from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from main.forms import ExpenseForm
from main.models import FinanceGroup, Expense


def index_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()

            # return HttpResponseRedirect('#greate')
    else:
        form = ExpenseForm()

    return render(request, 'main/index.html', {"form": form, "expenses": Expense.objects.all()})


def index(request):
    return render(request, 'main/main.html')
