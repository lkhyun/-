from django.db import models
#User 모델 정의
class User(models.Model):
    user_id = models.CharField(max_length=20, unique=True, verbose_name='유저 아이디')
    user_pw = models.CharField(max_length=30, verbose_name='비밀번호')
    user_name = models.CharField(max_length=15, unique=True, verbose_name='이름')
    user_email = models.EmailField(max_length=100, unique=True, verbose_name="이메일")
    user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="계정생성시간")

#객체를 문자열로 표현하는 방법 정의
def __str__(self):
    return self.user_name

#테이블의 이름을 user로 설정하고 읽기 쉬운 이름을 정의
class Meta:
    db_table = 'user'
    verbose_name = '유저'
    verbose_name_plural = '유저'   
