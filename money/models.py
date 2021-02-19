from django.db import models

# Create your models here.
class User(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    password    = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name
    

class TransactionType(models.Model):
    txn_type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.txn_type
    

class Transaction(models.Model):
    transaction_name    = models.CharField(max_length=2000)
    transaction_summary = models.TextField()
    transaction_date    = models.DateTimeField(null=False)
    transaction_amount  = models.IntegerField(blank=True)
    transaction_type    = models.CharField(max_length=200)
    isAnExpense         = models.CharField(max_length=1)
    # user                = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.transaction_name
    
    
    
    
