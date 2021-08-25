from tracker.models import Expense
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Expense
from .forms import ExpenseForm
import datetime
from datetime import timedelta
from django.db.models import Sum

today = datetime.date.today()
previous_month = today - timedelta(days=31)
# Create your views here.

class IndexView(ListView):
    model = Expense


def expense_form(request):
    budget = 5000
    alert = ''
    form = ExpenseForm()
    total_amount = Expense.objects.all().aggregate(Sum('amount'))
    if total_amount['amount__sum'] > budget:
        alert = 'You have exceeded allocated budget'

    return render(request, 'tracker/add_expense.html', {'ExpenseForm': form, 'alert':alert})

def report(request):
    if request.GET:
        report_type = request.GET['report_type']
        if report_type == 'current_month':
            data = Expense.objects.filter(created_at__month=today.month)
        elif report_type == 'previous_month':
            data = Expense.objects.filter(created_at__month=previous_month.month)
        elif report_type == 'current_year':
            data = Expense.objects.filter(created_at__year=today.year)
        else:
            data = Expense.objects.all()
    else:
        data = Expense.objects.all()
    return render(request, 'tracker/report.html', {'ExpenseData': data})
