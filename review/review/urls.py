from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plainly-book-review/', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/plainly-book-review/')),
    path('accounts/password_change_form/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change_form'),
    path('accounts/password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('accounts/password_reset_form/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html', subject_template_name='registration/password_reset_email_subject.txt', from_email=' aikawa.shota24@gmail.com '), name='password_reset'),
    path('accounts/password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_mail_done.html'), name='password_reset_done'),
    path('accounts/password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirmation.html'), name='password_reset_confirm'),
    path('accounts/password_reset_finish/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_finish.html'), name='password_reset_complete'),
]
