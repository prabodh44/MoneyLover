from django.shortcuts import render, redirect
from money.models import User, Transaction, TransactionType
from django.http import JsonResponse

from django.db.models import Sum
import datetime

# Create your views here.
def index_view(request):
    incomes   = getSumOfAllIncomes()
    expenses  = getSumOfAllExpenses()
    remaining = getSumOfAllIncomes() - getSumOfAllExpenses() 
    
    
    context = {
        'incomes':incomes,
        'expenses':expenses,
        'remaining':remaining,
        
    }
    return render(request, 'money/index.html', context)

def addTransaction_view(request):
    transaction_types = TransactionType.objects.all()
    if(request.method == "POST"):
        txn_name = request.POST["txn_name"]
        txn_summary = request.POST["txn_summary"]
        txn_amount = request.POST["txn_amount"]
        txn_type = TransactionType.objects.get(txn_type=request.POST["txn_type"])
        
        transaction = Transaction.objects.create(
            transaction_name=txn_name,
            transaction_summary=txn_summary,
            transaction_date=datetime.datetime.now(),
            transaction_amount=txn_amount,
            transaction_type=txn_type,
        )
        
        transaction.save()
        
        transactions = Transaction.objects.filter(transaction_type__isAnExpense="yes")
        txn_total = getSumOfAllExpenses()

        return render(request, 'money/transactionList.html', {'transactions':transactions, 'txn_total':txn_total, 'transaction_types':transaction_types })
    return render(request, 'money/addTransaction.html', {'transaction_types':transaction_types})

def getSumOfAllExpenses():
    total = Transaction.objects.filter(transaction_type__isAnExpense="yes").aggregate(Sum('transaction_amount'))
    txn_total = total["transaction_amount__sum"]
    return txn_total

def getSumOfAllIncomes():
     total = Transaction.objects.filter(transaction_type__isAnExpense="no").aggregate(Sum('transaction_amount'))
     txn_total = total["transaction_amount__sum"]
     return txn_total
    

# def transactionList_view(request):
#     transactions = Transaction.objects.filter(transaction_type__isAnExpense="yes")
#     txn_total = getSumOfAllExpenses()
#     print("transaction list")
#     print(transactions)
    
     
#     context = {
#         'transactions':transactions,
#         'txn_total':txn_total,
#     }
#     return render(request, "money/transactionList.html", context)

def addTransactionType_view(request):
    return render(request, "money/addTransactionTypes.html", {})

def transactions_view(request):
    transactions = Transaction.objects.filter(transaction_type__isAnExpense="yes")
    transaction_types = TransactionType.objects.all()
    txn_total = getSumOfAllExpenses()
    if(request.method == "POST"):
        sortBytransactionTypes = request.POST["sortBytransactionTypes"]
        transactions = listQueriesByType(transactions, sortBytransactionTypes)
        total = Transaction.objects.filter(transaction_type__txn_type=sortBytransactionTypes).aggregate(Sum('transaction_amount'))
        txn_total =  total["transaction_amount__sum"]

    return render(request, 'money/transactionList.html', {'transaction_types':transaction_types, 'transactions':transactions, 'txn_total':txn_total})

def listQueriesByType(transactions, sortBytransactionTypes):
    sortedTransactions = transactions.filter(transaction_type__txn_type=sortBytransactionTypes)
    return sortedTransactions


def transactionTypes_view(request):
    if request.method == "POST":
        txn_type = request.POST["txn_type"]
        expenseType = request.POST["isAnExpense"]
        if expenseType == "income":
            isAnExpense = "no"
        else:
            isAnExpense = "yes"
        
        transaction_type = TransactionType.objects.create(txn_type=txn_type, isAnExpense=isAnExpense)
        transaction_type.save()
        return redirect('index')
    return render(request, 'money/addTransactionTypes.html', {})

def login_view(request):
    return render(request, 'money/login.html', {})

def logout_view(request):
    return render(request, "money/login.html", {})

def pie_chart_view(request):
    labels = []
    data = []
    
    querySet = Transaction.objects.order_by('-transaction_amount')[:5]
    for q in querySet:
        labels.append(q.transaction_name)
        data.append(q.transaction_amount)
        
    return JsonResponse(data={
        'labels':labels,
        'data':data,
    })
    
    
