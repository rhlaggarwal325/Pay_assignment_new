from django.db import models

# Create your models here.

class Wallet(models.Model):
    username = models.CharField(max_length=128, unique=True)
    balance = models.IntegerField(default=0)
    money_added = models.IntegerField(default=0)
    money_sent = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

# transact_type = (
#     ("Add", "Add"),
#     ("Receive", "Receive"),
#     ("Sent", "Sent"),
# )

# class Transaction(models.Model):
#     transaction_type = models.CharField(max_length=10, choices=transact_type)
#     wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
#     amount = models.IntegerField()
#     transaction_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.wallet.username + " " + self.transaction_type + " " + str(self.id)
