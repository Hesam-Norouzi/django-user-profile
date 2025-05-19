from django.urls import path
from .views import register_view, home_view, profile_view, profile_edit_view
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)