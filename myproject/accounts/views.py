from django.shortcuts import render,redirect
from django.contrib import auth
from .models import User
from django.contrib.auth.models import User as djUser

# Create your views here.

def login(request):
    #POST 요청이 들어오면 로그인 처리를 해주고
    if request.method == "POST":
        userid = request.POST['userid']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('home') #login이 성공했을때 리디렉션하는것을 LOGIN_REDIRECT_URL="/"을 settings.py에 적어 구현할 수 있다. 
        else:
            return render(request, 'login.html')

    #GET 요청이 들어오면 login form을 담고 있는 login.html을 띄워줌
    else:
        return render(request, 'login.html')
#logout하게되면 계정 로그아웃하고 홈으로 리디렉션
def logout(request):
    auth.logout(request)
    return redirect('home')
            

#회원가입
def signup(request):
    #GET 요청이 들어오면 회원가입 페이지를 렌더링해주기
    if request.method =='GET':
        return render(request, 'signup.html')
    #POST요청이 오면 사용자가 입력한 정보를 처리
    elif request.method == 'POST':
        user_id = request.POST.get('id','')
        user_pw = request.POST.get('pw','')
        user_pw_confirm = request.POST.get('pw-confirm','')
        user_name = request.POST.get('name','')
        user_email = request.POST.get('email','')

        #하나라도 입력되지 않은 정보가 있다면 다시 회원가입을 하게끔 하기
        if (user_id or user_pw or user_pw_confirm or user_name or user_email) == '':
            return redirect('signup')
        #비밀번호 입력한 것이 비밀번호 확인과 일치하지 않으면 다시 회원가입
        elif user_pw != user_pw_confirm:
            return redirect('signup')
        #객체에 저장 후 데이터베이스에 계정 정보 저장    
        else:
            user = User(
                user_id = user_id,
                user_pw = user_pw,
                user_name = user_name,
                user_email = user_email
            )
            user.save()
            #계정 정보를 객체에 저장해 회원가입 후 바로 자동로그인이 되게끔 하기
            djuser = djUser.objects.create_user(
                username=request.POST['id'],
                password=request.POST['pw'],
                email=request.POST['email'],
            )
            auth.login(request, djuser)

        return redirect('home')
    else:
        return redirect('home')
