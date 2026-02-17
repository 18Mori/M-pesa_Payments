from django import forms

class PaymentForm(forms.Form):
  phone_number=forms.CharField(required=True, label='Phone Number', max_length=10)
  amount=forms.IntegerField(required=True, label='Amount', max_value=498400, min_value=1, error_messages={'max_value': 'Amount cannot exceed 498,400 KSH'})