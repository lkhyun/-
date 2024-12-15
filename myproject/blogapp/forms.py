from socket import fromshare
from django import forms
from .models import Post, Comment
#게시물 모델 폼
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body','photo']
#댓글 모델 폼
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
#속성 정의
widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'body': forms.CharField(),
        }