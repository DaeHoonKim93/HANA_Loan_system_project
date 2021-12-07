from django.db import models
from fcuser.models import Fcuser


class Worksheet(models.Model):

    emp_name = models.CharField(max_length=32,
                                verbose_name='직원 이름',
                                null='True')

    customer_id = models.IntegerField(verbose_name='고객번호', default=12345678)

    customer_name = models.CharField(max_length=256,
                                     verbose_name='고객명',
                                     null='False')
    loan_start_date = models.DateField(verbose_name='실행 예정일', null='False')

    loan_product = models.CharField(max_length=30,
                                    verbose_name='대출상품',
                                    null='True')
    # loan_product = models.ForeignKey("Process",
    #                                  related_name="process",
    #                                  on_delete=models.CASCADE,
    #                                  db_column="loan_product",
    #                                  null='False')
    loan_amount = models.IntegerField(verbose_name='대출금액', null='True')

    loan_condition = models.BooleanField(default=False)
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


class Process(models.Model):
    #pk -> id
    loan_product = models.CharField(max_length=30,
                                    verbose_name='대출상품',
                                    null='True')
    process_index = models.IntegerField(verbose_name='진행순번', null='True')
    process_step = models.CharField(max_length=30,
                                    verbose_name='진행단계',
                                    null='True')

    def __str__(self):
        return self.loan_product

    class Meta:
        db_table = 'Process'
        verbose_name = '진행척도관리'
        verbose_name_plural = '진행척도관리'


class loan_product(models.Model):
    #pk -> id
    loan_product_name = models.CharField(max_length=30,
                                         verbose_name='대출상품이름',
                                         null='False')

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'loan_product'
        verbose_name = '대출상품이름'
        verbose_name_plural = '대출상품이름'


class loan_product2(models.Model):
    #pk -> id
    id2 = models.IntegerField(verbose_name='상품코드', null='False')
    loan_product_name = models.CharField(max_length=30,
                                         verbose_name='대출상품이름',
                                         null='False')

    def __str__(self):
        return self.loan_product_name

    class Meta:
        db_table = 'loan_product2'
        verbose_name = '대출상품이름2'
        verbose_name_plural = '대출상품이름2'


# class loan_process(models.Model):
#     #pk -> id
#     loan_product_id = models.ForeignKey("loan_product",related_name="loan_product",
#                                      on_delete=models.CASCADE,
#                                      db_column="loan_product",
#                                      null='False')

#     loan_process_level = models.IntegerField(verbose_name='진행단계', null='False')
#     loan_process_name = models.CharField(max_length=30,
#                                     verbose_name='진행단계',
#                                     null='True')

#     def __str__(self):
#         return self.loan_product

#     class Meta:
#         db_table = 'Process'
#         verbose_name = '진행척도관리'
#         verbose_name_plural = '진행척도관리'
