from django.conf.urls import url
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pay',views.WalletViewSet)

urlpatterns = [
    path('add/<int:pk>/', views.AddMoneyView.as_view(),),
    path('send/<int:pk>/', views.SendMoneyView.as_view(),),
    path('balance/<int:pk>/', views.CheckBalanceView.as_view(),),
]   

urlpatterns += router.urls