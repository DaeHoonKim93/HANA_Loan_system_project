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

    



    
    
    # title = models.CharField(max_length=128,
    #                          verbose_name='제목')  # 명명으로 사용자명으로 보이게된다.

    # contents = models.TextField(verbose_name='내용')
    # writer = models.ForeignKey(
    #     'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='작성자')
    # # on_delete는 게시글을 만들었을때, 사용자가 탈퇴할 경우 사용자가 쓴 게시글을 같이 삭제해주는 것 ! CASCADE

    # registered_dttm = models.DateTimeField(auto_now_add=True,  # fcuser라는 객체가 저장되는 시간이 자동으로 들어간다.
    #                                        verbose_name='등록시간')  # dttm -> datetime의 약자

    # def __str__(self):
    #     return self.title

    # class Meta:
    #     db_table = 'fastcampus_board'
    #     verbose_name = '패스트캠퍼스 게시글'
    #     verbose_name_plural = '패스트캠퍼스 게시글'
