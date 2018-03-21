# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from expense_app.models import Expense
from expense_app.forms import ExpenseForm


def home(request):
    content = Expense.objects.all().order_by('-date')
    summary = {}
    temp_date = 0
    sum = 0
    count = 0
    for item in content:
        if count == 0:
            temp_date = item.date.date()
            count = 1
        if item.date.date() == temp_date:
            print(item.cost)
            sum = sum + item.cost
            summary[str(item.date.date())] = sum
        else:
            sum = item.cost
            summary[str(item.date.date())] = item.cost
        temp_date = item.date.date()
    print(summary)
    return render(request, 'expense_app/home.html',
                  {'content': content, 'summary': summary})


class ExpenseFormView(View):
    form_class = ExpenseForm
    template_name = 'expense_app/expense_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            expense_detail = form.save()
        return render(request, self.template_name, {'form': form})
