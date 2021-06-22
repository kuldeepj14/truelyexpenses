from django.shortcuts import render, redirect
from .models import Source, UserIncome
from django.core.paginator import Paginator
from userpreferences.models import UserPreference
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse

# Create your views here.



def search_incomes(request):
    if request.method == 'POST':

        search_str = json.loads(request.body).get('searchText')
        
        income = UserIncome.objects.filter(amount__istartswith=search_str, owner = request.user) | UserIncome.objects.filter(date__istartswith=search_str, owner = request.user) | UserIncome.objects.filter(description__icontains=search_str, owner = request.user) | UserIncome.objects.filter(source__icontains=search_str, owner = request.user)
        # icontains filter let search regardless case of a string,  
        data = income.values()

        return JsonResponse(list(data), safe=False)
        
         


@login_required(login_url='/authentication/login')
def index(request):
    categories = Source.objects.all()
    income = UserIncome.objects.filter(owner=request.user)
    paginator = Paginator(income, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    currency = UserPreference.objects.get(user=request.user).currency
    context = {
        'income' : income,
        'page_obj' : page_obj,
        'currency' : currency,
    }

    return render(request, 'income/index.html', context)


sources = Source.objects.all()


def add_income(request):
    
    context = {
            'sources':sources,
            'values': request.POST
        }
    if request.method == "GET":        
        return render(request, 'income/add_income.html', context)

    if request.method == "POST":
        
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'income/add_income.html', context)
        # by adding Value attribute in description input in html the user data can be made visible without submitting and refereshing page    
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'income/add_income.html', context)

        UserIncome.objects.create(owner=request.user, amount=amount, date=date, source=source, description=description)
        messages.success(request, 'Record saved succesfully')
        return redirect('income')
    return render(request, 'income/add_income.html', context)


@login_required(login_url='/authentication/login')
def income_edit(request, id):
    income = UserIncome.objects.get(pk=id)
    context = {
        'income' : income,
        'values' : income,
        'sources':sources,
    }
    if request.method == 'GET':
        # import pdb
        # pdb.set_trace()
        return render(request, 'income/edit_income.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'income/edit_income.html', context)
        # by adding Value attribute in description input in html the user data can be made visible without submitting and refereshing page    
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'income/edit_income.html', context)

        income.owner=request.user
        income.amount=amount 
        income.date=date 
        income.source=source
        income.description=description
        income.save()
        messages.success(request, 'Record Updated succesfully')
        return redirect('income')

@login_required(login_url='/authentication/login')
def delete_income(request, id):
    income = UserIncome.objects.get(pk=id)
    income.delete()
    messages.success(request, 'Record Removed Successfully')
    return redirect('income')
