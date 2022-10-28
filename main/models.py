from django.db import models

from users.models import User

standard_groups = ["Питание", "Коммунальные платежи", "Одежда", "Образование", "Отдых", "Разное"]


class FinanceGroup(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f"{self.name}"


class Expense(models.Model):
    name = models.CharField(max_length=255, default="", null=True)
    amount = models.FloatField(verbose_name="сумма")
    finance_group = models.ForeignKey(FinanceGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
