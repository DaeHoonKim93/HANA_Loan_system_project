from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')  # 명명으로 사용자명으로 보이게된다.

    useremail = models.EmailField(max_length=128,
                                  verbose_name='사용자 이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')

    registered_dttm = models.DateTimeField(auto_now_add=True,  # fcuser라는 객체가 저장되는 시간이 자동으로 들어간다.
                                           verbose_name='등록시간')  # dttm -> datetime의 약자

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '직원명단'
        verbose_name_plural = '직원명단'
