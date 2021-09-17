from django.contrib import admin
from .models import Wallet

# Register your models here.
class WalletAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'balance', 'money_added', 'money_sent']

admin.site.register(Wallet, WalletAdmin)