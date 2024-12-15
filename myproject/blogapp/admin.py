import imp
from django.contrib import admin
from .models import Post, Comment
#관리자 페이지에 게시물과 댓글 등록
admin.site.register(Post)
admin.site.register(Comment)