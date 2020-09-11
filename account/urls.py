from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # post views
    # url(r'^login/', views.user_login, name='login'),
    url(r'^login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^$', views.dashboard, name='dashboard'),
    # password change urls
    url(r'^password_change/',
     auth_views.PasswordChangeView.as_view(),
     name='password_change'),
    url(r'^password_change/done/',
      auth_views.PasswordChangeDoneView.as_view(),
      name='password_change_done'),
    # reset password urls
    url(r'^password_reset/',
      auth_views.PasswordResetView.as_view(),
      name='password_reset'),
    url(r'^password_reset/done/',
      auth_views.PasswordResetDoneView.as_view(),
      name='password_reset_done'),
    url(r'^reset/<uidb64>/<token>/',
      auth_views.PasswordResetConfirmView.as_view(),
      name='password_reset_confirm'),
    url(r'^reset/done/',
      auth_views.PasswordResetCompleteView.as_view(),
      name='password_reset_complete'),
    url(r'^$', include('django.contrib.auth.urls')),
    url(r'^register/', views.register, name='register'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^users/', views.user_list, name='user_list'),
    url(r'^users/(?P<username>\w{0,50})/$', views.user_detail, name='user_detail'),
    url(r'^users/follow/', views.user_follow, name='user_follow'),

]
