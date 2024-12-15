from django.shortcuts import render

# 각각 원하는 정보를 보여주기 위한 페이지 렌더링 함수 정의
def home(request):
    return render(request, 'about.html')

def gpu(request):
    return render(request,'gpu.html')

def mainboard(request):
    return render(request,'mainboard.html')

def power(request):
    return render(request,'power.html')

def ram(request):
    return render(request,'ram.html')

def ssd(request):
    return render(request,'ssd.html')