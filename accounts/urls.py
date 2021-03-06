from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from core.templatetags.check_recaptcha import check_recaptcha
from .views import UserUpdateView, gitlab_auth, UserSignupView, UserLoginView

urlpatterns = [
    url(r'^signup/$', check_recaptcha(UserSignupView.as_view()), name='signup'),
    url(r'^login/$', check_recaptcha(UserLoginView.as_view()), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'),
        name='password_change_done'),
    url(r'^view/$', UserUpdateView.as_view(), name='view_account'),
    url(r'^gitlab/callback/$', gitlab_auth, name='gitlab.callback')
]