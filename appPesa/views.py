from django.shortcuts import render
from .forms import *

def payment_view(request):
  form=PaymentForm()
  return render(request,'Home-pay-view.html',{'form':form})