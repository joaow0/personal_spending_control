from django.shortcuts import render, HttpResponse, redirect
from .form import ExpensesForm
from .models import Expenses

def create_expenses(request):

    if request.method == 'GET':
        category = request.GET.get('category')
        if category:
            expenses = Expenses.objects.filter(category=category)
        else:
            expenses = Expenses.objects.all()

        context = {
            'form': ExpensesForm(),
            'data': expenses,
            'categories': Expenses.CHOICES,
        }
        return render(request, 'expenses.html', context=context)
    
    elif request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_expenses')
        else:
            return HttpResponse(form.errors)

