from django.shortcuts import render, redirect
from money.models import User, Transaction, TransactionType

from django.db.models import Sum
import datetime

# Create your views here.
def index_view(request):
    return render(request, 'money/index.html', {})

def addTransaction_view(request):
    transaction_types = TransactionType.objects.all()
    if(request.method == "POST"):
        txn_name = request.POST["txn_name"]
        txn_summary = request.POST["txn_summary"]
        txn_amount = request.POST["txn_amount"]
        txn_type = request.POST["txn_type"]
        
        transaction = Transaction.objects.create(
            transaction_name=txn_name,
            transaction_summary=txn_summary,
            transaction_date=datetime.datetime.now(),
            transaction_amount=txn_amount,
            transaction_type=txn_type,
        )
        
        transaction.save()
        
        transactions = Transaction.objects.all()
        total = Transaction.objects.aggregate(Sum('transaction_amount'))
        txn_total = total["transaction_amount__sum"]

        return render(request, 'money/transactionList.html', {'transactions':transactions, 'txn_total':txn_total, 'transaction_types':transaction_types })
    return render(request, 'money/addTransaction.html', {'transaction_types':transaction_types})

def transactionList_view(request):
    transactions = Transaction.objects.all()
    
    print("transaction types")
    print(transaction_types)
    context = {
        'transactions':transactions,
        'transaction_types':transaction_types
    }
    return render(request, "money/transactionList.html", context)

def addTransactionType_view(request):
    return render(request, "money/addTransactionTypes.html", {})

def transactions_view(request):
    transactions = Transaction.objects.all()
    transaction_types = TransactionType.objects.all()
    total = Transaction.objects.aggregate(Sum('transaction_amount'))
    txn_total = total["transaction_amount__sum"]
    if(request.method == "POST"):
        sortBytransactionTypes = request.POST["sortBytransactionTypes"]
        transactions = listQueriesByType(transactions, sortBytransactionTypes)
        total = Transaction.objects.filter(transaction_type=sortBytransactionTypes).aggregate(Sum('transaction_amount'))
        txn_total =  total["transaction_amount__sum"]

    return render(request, 'money/transactionList.html', {'transactions':transactions, 'txn_total':txn_total, 'transaction_types':transaction_types, })

def listQueriesByType(transactions, sortBytransactionTypes):
    sortedTransactions = transactions.filter(transaction_type=sortBytransactionTypes)
    return sortedTransactions


def transactionTypes_view(request):
    if request.method == "POST":
        txn_type = request.POST["txn_type"]
        transaction_type = TransactionType.objects.create(txn_type=txn_type)
        transaction_type.save()
        return redirect('index')
    return render(request, 'money/addTransactionTypes.html', {})

def login_view(request):
    return render(request, 'money/login.html', {})
    
