from django.shortcuts import render

from everyday.models import Expenses


# Create your views here.
def index(request):
    return render(request, 'everyday/index.html')


def expenses(request):
    expenses = Expenses.objects.order_by('date').latest
    if not expenses:
        expenses = Expenses
    context = {'expenses': expenses}
    return render(request, 'everyday/expenses.html', context)
