# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView

from expense_app.models import Expense
from expense_app.forms import ExpenseForm
from expense_app.serializers import ExpenseSerializer


def index(request):
    return render(request, 'index.html')


def home(request):
    """Veiw function of home retrieving the expense content sorted in reverse
    order by date and summary of expense """
    content = Expense.objects.all().order_by('-date')
    # Dictionary
    summary = {}

    # temporary variables
    temp_date = 0
    sum = 0
    count = 0

    # looping through content and calculating the cost in the order of date
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

    # print the summary of cost
    print(summary)

    # rendering template
    return render(request, 'expense_app/home.html',
                  {'content': content, 'summary': summary})


class ExpenseFormView(View):
    """Inbuilt Form view class to display forms and handling 'GET' and 'POST'
    requests """
    form_class = ExpenseForm
    template_name = 'expense_app/expense_form.html'

    # returns the form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # add details to expense model if valid
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            expense_detail = form.save()
            # flash message
            messages.success(request, "Added Successfully")
            return redirect('/')
        else:
            # flash message
            messages.error(request, "Please enter details correctly")
            return render(request, self.template_name, {'form': form})


class ExpanseAPI(APIView):
    def get(self, request):
        content = Expense.objects.all()
        serializer = ExpenseSerializer(content, many=True)
        return Response(serializer.data)
