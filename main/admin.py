from django.contrib import admin

# Register your models here.
from main.models import FinanceGroup, Expense

admin.site.register(FinanceGroup)
admin.site.register(Expense)