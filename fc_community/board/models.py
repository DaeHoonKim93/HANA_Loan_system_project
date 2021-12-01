from django.db import models
from fcuser.models import Fcuser
# Create your models here.
class Worksheet(models.Model):

    customer_id = models.IntegerField(verbose_name='고객번호', default=12345678)

    customer_name = models.CharField(
        max_length=256, verbose_name='고객명', null='False')

    loan_product = models.CharField(max_length= 30 ,verbose_name='대출상품', null='True')

    loan_amount = models.IntegerField(verbose_name='대출금액', null='True')

    description = models.TextField(verbose_name='메모')
    phone_number = models.CharField(max_length = 13, verbose_name='핸드폰번호', null = True)
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')
    loan_start_date = models.DateField(verbose_name='실행 예정일', null='False')

    emp_name = models.CharField(max_length= 32 ,verbose_name='직원 이름', null='True')

    def __str__(self):
        return self.customer_name

    class Meta:
        db_table = 'WorkSheet'
        verbose_name = '업무목록'
        verbose_name_plural = '업무목록'

    
class 