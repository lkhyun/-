"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views
from accounts import views as accounts_views
from blogapp import views as blog_views
from django.conf.urls.static import static
from django.conf import settings
# url에 따라 함수들을 매핑하는 곳
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('community',blog_views.community, name='community'),
    path('login/',accounts_views.login, name='login'),
    path('logout/',accounts_views.logout, name='logout'),
    path('signup/',accounts_views.signup, name='signup'),
    path('gpu/', views.gpu, name= 'gpu'),
    path('mainboard/', views.mainboard, name= 'mainboard'),
    path('power/', views.power, name= 'power'),
    path('ram/', views.ram, name= 'ram'),
    path('ssd/', views.ssd, name= 'ssd'),
    path('modelformcreate/', blog_views.modelformcreate, name='modelformcreate'),
    path('detail/<int:post_id>', blog_views.detail, name="detail"),
    path('create_comment/<int:post_id>', blog_views.create_comment, name="create_comment"),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #static 사용 세팅