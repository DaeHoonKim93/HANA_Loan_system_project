from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class RegisterForm(forms.Form):
    emp_id = forms.IntegerField(
        error_messages={
            'required': '직원번호를 을 입력해주세요.'
        }, label='직원번호'
    )
    emp_name = forms.CharField(
        error_messages={
            'required': '직원이름을 입력해주세요.'
        }, label='직원이름'
    )

    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()  # 이건뭐지!?
        emp_id = cleaned_data.get('emp_id')
        emp_name = cleaned_data.get('emp_name')

        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')

class LoginForm(forms.Form):
    emp_id = forms.IntegerField(
        error_messages={
            'required': '직원번호를 입력해주세요.'
        }, label='직원번호'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        emp_id = cleaned_data.get('emp_id')
        emp_name = cleaned_data.get('emp_name')

        password = cleaned_data.get('password')

        if emp_id and password:
            try:
                fcuser = Fcuser.objects.get(emp_id=emp_id)
            except Fcuser.DoesNotExist:
                self.add_error('emp_id', '아이디가 없습니다')
                return

            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다')


# class LoginForm(forms.Form):
#     emp_id = forms.IntegerField(label="직원번호", 
#             error_messages={'required' : "직원번호를 입력하세요"})
#     password = forms.CharField(widget=forms.PasswordInput, label="비밀번호",
#             error_messages={'required' : "비밀번호를 입력하세요"})
    
#     #valid inspection
    
#     def clean(self):
#         clean_data = super().clean()
#         emp_id = clean_data.get('emp_id')
#         password = clean_data.get('password')
        
#         if emp_id and password:
#             fcuser = Fcuser.objects.get(emp_id = emp_id)
            
#             if not check_password(password, fcuser.password) :
#                 self.add_error('password', '비밀번호가 틀렸습니다.')
#             else :
#                 self.emp_id = fcuser.id
                   
        
                
