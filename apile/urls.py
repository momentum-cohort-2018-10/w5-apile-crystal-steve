"""apile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from core.backends import MyRegistrationView -- this is part of having people create "something" - not sure this is applicable
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,)
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from core import views

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('', views.index, name='home'),
    path('accounts/password/reset/', PasswordResetView, {'template_name': 'registration/password_reset_form.html'}, name="password_reset"),
    path('accounts/password/reset/done/', PasswordResetDoneView, {'template_name': 'registration/password_reset_done.html'}, name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView, {'template_name': 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    path('accounts/password/done/', PasswordResetCompleteView,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<slug>/delete', views.delete_post, name='delete_post'),
    path('posts/<int:comment_id>/delete_comment', views.delete_comment, name='delete_comment'),
    path('posts/<slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug>/comment/', views.create_comment, name='create_comment'),
    path('posts/<slug>/edit/', views.edit_post, name='edit_post'),
    path('admin/', admin.site.urls),
]
