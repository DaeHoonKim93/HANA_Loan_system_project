from django import forms
from .models import Worksheet


class RegisterForm(forms.Form):
    customer_id = forms.IntegerField(
        error_messages={'required': '고객번호를 입력해주세요.'}, label='고객번호 입력해요')
    customer_name = forms.CharField(
        error_messages={'required': '고객명을 입력해주세요.'},
        max_length=64,
        label='고객명')
    phone_number = forms.CharField(error_messages={'required': '연락처를 입력해주세요.'},
                                   label='연락처')
    loan_product = forms.CharField(
        error_messages={'required': '대출상품을 입력해주세요.'}, label='대출상품')
    loan_amount = forms.IntegerField(
        error_messages={'required': '대출금액을 입력해주세요.'}, label='대출금액')
    description = forms.CharField(error_messages={'required': '메모를 입력해주세요.'},
                                  label='메모')

    def clean(self):
        cleaned_data = super().clean()
        customer_id = cleaned_data.get('customer_id')
        customer_name = cleaned_data.get('customer_name')
        loan_product = cleaned_data.get('loan_product')
        loan_amount = cleaned_data.get('loan_amount')
        description = cleaned_data.get('description')
        phone_number = cleaned_data.get('phone_number')

        if not (customer_id and customer_name and loan_product and loan_amount
                and description and phone_number):
            self.add_error('customer_name', '값이 없습니다')
            self.add_error('loan_amount', '값이 없습니다')
