from django.db import models
from fcuser.models import Fcuser


class Worksheet(models.Model):
    emp_name = models.CharField(max_length=32,
                                verbose_name='직원 이름',
                                null='True')

    customer_id = models.IntegerField(verbose_name='고객번호', default=001)

    customer_name = models.CharField(max_length=256,
                                     verbose_name='고객명',
                                     null='False')
    loan_start_date = models.DateField(verbose_name='실행 예정일', null='False')

    loan_product = models.CharField(max_length=30,
                                    verbose_name='대출상품',
                                    null='True')
    loan_amount = models.IntegerField(verbose_name='대출금액', null='True')

    loan_condition = models.CharField(max_length=10,
                                      verbose_name='상환조건',
                                      null='True')
    description = models.TextField(verbose_name='메모')
    phone_number = models.CharField(max_length=13,
                                    verbose_name='핸드폰번호',
                                    null=True)
    register_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='등록날짜')
    current_process_id = models.IntegerField(verbose_name='현재 진행 척도',
                                             default=1)

    def __str__(self):
        return self.customer_name

    class Meta:
        db_table = 'WorkSheet'
        verbose_name = '업무목록'
        verbose_name_plural = '업무목록'


class LoanProduct(models.Model):
    #pk -> id
    id = models.IntegerField(verbose_name='상품코드', null=False, primary_key=True)
    loan_product_name = models.CharField(max_length=30,
                                         verbose_name='대출상품이름',
                                         null='False')

    def __str__(self):
        return self.loan_product_name

    class Meta:
        db_table = 'loan_product'
        verbose_name = '대출상품이름'
        verbose_name_plural = '대출상품이름'


class LoanProcess(models.Model):
    loan_product = models.OneToOneField('LoanProduct',
                                        models.DO_NOTHING,
                                        primary_key=True)
    loan_process_level = models.IntegerField()
    loan_process_name = models.CharField(max_length=20)

    def __str__(self):
        return self.loan_process_name

    class Meta:
        db_table = 'loan_process'
        verbose_name = '대출업무 진행단계'
        verbose_name_plural = '대출업무 진행단계'

        unique_together = (('loan_product', 'loan_process_level'))


class TodoList(models.Model):
    emp_name = models.CharField(max_length=32,
                                verbose_name='직원 이름',
                                null='True')
    register_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='등록날짜')
    content = models.TextField(max_length=100)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'TodoList'
        verbose_name = '오늘의 할일'
        verbose_name_plural = '오늘의 할일'
