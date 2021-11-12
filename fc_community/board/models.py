from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목')  # 명명으로 사용자명으로 보이게된다.

    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey(
        'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='작성자')
    # on_delete는 게시글을 만들었을때, 사용자가 탈퇴할 경우 사용자가 쓴 게시글을 같이 삭제해주는 것 ! CASCADE

    registered_dttm = models.DateTimeField(auto_now_add=True,  # fcuser라는 객체가 저장되는 시간이 자동으로 들어간다.
                                           verbose_name='등록시간')  # dttm -> datetime의 약자

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'
