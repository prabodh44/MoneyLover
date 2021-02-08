from django.contrib import admin
from money.models import User, TransactionType, Transaction

# Register your models here.
admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(TransactionType)
