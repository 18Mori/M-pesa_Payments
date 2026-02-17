from django.urls import path
from .import views

urlpatterns = [
    path('', views.payment_view, name='payment_page'),
    path('callback/', views.pesa_callback, name='pesa_callback'),
    path('stk_status/', views.stk_status_view, name='stk_status'),
    # path('success/', views.success_view, name='success_page'),
]