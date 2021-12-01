# from django.db import models

# # Create your models here.


# class Worksheet(models.Model):

#     customer_id = models.IntegerField(verbose_name='고객번호', default=12345678)

#     customer_name = models.CharField(
#         max_length=256, verbose_name='고객명', null='False')

#     loan_product = models.CharField(max_length= 30 ,verbose_name='대출상품', null='True')
#     loan_amount = models.IntegerField(verbose_name='대출금액', null='True')

#     description = models.TextField(verbose_name='메모')
#     phone_number = models.CharField(max_length = 13, verbose_name='핸드폰번호', null = True)
#     register_date = models.DateTimeField(
#         auto_now_add=True, verbose_name='등록날짜')


#     # emp_name = models.ForeignKey(
#     #     'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='작성자', null = 'True')


#     def __str__(self):
#         return self.customer_name

#     class Meta:
#         db_table = 'WorkSheet'
#         verbose_name = '업무목록'
#         verbose_name_plural = '업무목록'




    




from django.db import models
from fcuser.models import Fcuser



class Worksheet(models.Model):

    customer_id = models.IntegerField(verbose_name='고객번호', default=12345678)

    customer_name = models.CharField(
        max_length=256, verbose_name='고객명', null='False')

    loan_product = models.CharField(max_length= 30 ,verbose_name='대출상품', null='True')
    # loan_product = models.ForeignKey("Worksheet", related_name="worksheet", on_delete=models.CASCADE, db_column="loan_product")
    

    loan_amount = models.IntegerField(verbose_name='대출금액', null='True')

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

<<<<<<< HEAD

class Process(models.Model):
    loan_product = models.CharField(max_length= 30 ,verbose_name='대출상품', null='True')
    process_index = models.IntegerField(verbose_name='진행순번', null='True')
    process_step =  models.CharField(max_length= 30 ,verbose_name='진행단계', null='True')

    def __str__(self):
        return self.loan_product

    class Meta:
        db_table = 'Process'
        verbose_name = '진행척도관리'
        verbose_name_plural = '진행척도관리' 
=======
    
class 
>>>>>>> 65d5511aede8a6b143862a5730275e3a22339882
