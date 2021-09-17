from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Wallet
from .serializers import WalletSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

# Create your views here.
class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class AddMoneyView(APIView):

    def patch(self, request, pk):
        wallet = Wallet.objects.get(id=pk)
        data = {"balance": wallet.balance + request.data["amount"], "money_added": wallet.money_added + request.data["amount"]}
        serialized = WalletSerializer(wallet, data = data, partial=True)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors)

class SendMoneyView(APIView):
    
    def patch(self, request, pk):
        sender = Wallet.objects.get(id = pk)
        receiver = Wallet.objects.get(username = request.data["username"])
        sender_data = {"balance": sender.balance - request.data["amount"], "money_sent": sender.money_sent + request.data["amount"]}
        receiver_data = {"balance": receiver.balance + request.data["amount"]}

        sender_serialized = WalletSerializer(sender, data=sender_data, partial=True)
        receiver_serialized = WalletSerializer(receiver, data=receiver_data, partial=True)

        if sender_serialized.is_valid() and receiver_serialized.is_valid():
            sender_serialized.save()
            receiver_serialized.save()
            return Response(sender_serialized.data)
        return Response(sender_serialized.errors)

class CheckBalanceView(generics.GenericAPIView):
    # queryset = Wallet.objects.values('balance')

    def get(self, request, pk):
        return Response({"balance":Wallet.objects.get(id = pk).balance})