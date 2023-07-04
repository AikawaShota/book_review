from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('close_account_confirm/', views.close_account_confirm, name='close_account_confirm'),
    path('close_account/', views.close_account, name='close_account'),
    path('account/', views.account, name='account'),
]