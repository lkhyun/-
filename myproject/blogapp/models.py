from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#게시글 모델 정의
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='post_photo') #사진은 넣어도 되고 안넣어도 됨 upload_to는 업로드 되는 경로
    date = models.DateTimeField(auto_now_add=True)#자동으로 생성 시간 저장
    author = models.ForeignKey(User, on_delete=models.CASCADE)#User 계정정보가 삭제되면 게시물도 모두 삭제되게끔 속성 넣어주기

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment