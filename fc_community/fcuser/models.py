from django.db import models

# Create your models here.


class Fcuser(models.Model):
    emp_name = models.CharField(max_length=32,
                                verbose_name='직원 이름', null = 'True') 

    emp_id = models.IntegerField(verbose_name='직원 번호' , null = 'True')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')

    registered_dttm = models.DateTimeField(auto_now_add=True,  # fcuser라는 객체가 저장되는 시간이 자동으로 들어간다.
                                           verbose_name='등록시간')  # dttm -> datetime의 약자

    def __str__(self):
        return self.emp_name

    class Meta:
        db_table = 'emp_list'
        verbose_name = '직원명단'
        verbose_name_plural = '직원명단'
