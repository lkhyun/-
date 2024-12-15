from django.contrib import admin
from .models import User

# User model을 관리자 사이트에 등록하기
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    #보여질 필드 특정하기
    list_display = (
        'user_id',
        'user_pw',
        'user_name',
        'user_email',
        'user_register_dttm'
    )
