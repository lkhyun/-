from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostModelForm, CommentForm
#커뮤니티 페이지를 보여주는 함수
def community(request):
    posts=Post.objects.filter().order_by('-date')#게시물을 시간순으로 정렬하고
    return render(request, 'index.html', {'posts':posts})#게시물 목록과 함께 index.html을 렌더링

#모델 폼으로 게시물 생성
def modelformcreate(request):
    #POST나 FILES 요청이면 폼을 생성해 유효한지 검사한 후 
    if request.method == 'POST'  or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid(): #유효하다면
            unfinished = form.save(commit=False) #임시로 저장해 둔 후
            unfinished.author = request.user #글쓴이를 현재 요청한 사람으로
            unfinished.save() #저장
            return redirect('community')#다시 리디렉션

    #GET요청이라면 빈 게시물 폼 보여줘서 입력받도록
    else:
        form = PostModelForm()
    return render(request, 'form_create.html', {'form':form})

#게시물 상세정보 보여주기 없다면 에러표시
def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail' : post_detail, 'comment_form' : comment_form})

#댓글 생성
def create_comment(request, post_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk = post_id)
        finished_form.save()

    return redirect('detail', post_id)