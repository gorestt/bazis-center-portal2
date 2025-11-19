from django.urls import path
from . import views

app_name = 'docsapp'

urlpatterns = [
    path('', views.docs_public, name='docs_public'),
    path('manage/', views.docs_manage, name='docs_manage'),
]
