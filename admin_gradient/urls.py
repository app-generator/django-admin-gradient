from django.urls import path
from admin_gradient import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #pages
    path('', views.index, name = 'index'),
    path('bc-typography/', views.bc_typography, name = 'bc_typography'),
    path('icon-feather/', views.icon_feather, name = 'icon_feather'),
    path('tbl-bootstrap/', views.tbl_bootstrap, name = 'tbl_bootstrap'),
    path('chart-apex/', views.chart_apex, name = 'chart_apex'),
    path('map-google/', views.map_google, name = 'map_google'),
    path('sample-page/', views.sample_page, name = 'sample_page'),
    path('user-profile/', views.user_profile, name = 'user_profile'),
    path('accounts/auth-signup/', views.auth_signup, name = 'auth_signup'),
    path('accounts/auth-signin/', views.AuthSignin.as_view(), name='auth_signin'),
    path('accounts/forgot-password/', views.UserPasswordResetView.as_view(), name='forgot_password'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
]
