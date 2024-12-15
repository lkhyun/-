from django.apps import AppConfig

#모델 생성시 자동으로 정수키를 생성
class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapp'
