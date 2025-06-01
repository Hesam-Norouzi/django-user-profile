from django.urls import path
from .views import register_view, home_view, profile_view, profile_edit_view, delete_account_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', register_view, name='register'),
    path('', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('edit_profile/', profile_edit_view, name='edit_profile'),
    path('password_change/', 
         auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), 
         name='password_change'),

    path('password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), 
         name='password_change_done'),
    path('delete/', delete_account_view, name='delete_account'),
    path('password-reset/', auth_views.PasswordResetView.as_view(extra_email_context = {"protocol": "https", "domain": "django.hesamnorouzi.ir"}), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)