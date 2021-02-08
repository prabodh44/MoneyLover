from django.shortcuts import render, redirect
from money.models import User, Transaction, TransactionType

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
        
        txn = Transaction.objects.create(
            transaction_name=txn_name,
            transaction_summary=txn_summary,
            transaction_amount=txn_amount,
            txn_type=txn_type,
        )
        
        txn.save()
        
        return render(request, 'money/transactionList.html', {})
    return render(request, 'money/addTransaction.html', {'transaction_types':transaction_types})

def transactionList_view(request):
    return render(request, "money/transactionDetail.html", {})
