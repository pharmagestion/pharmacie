from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('login/', views.SignInFormView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.SignUpFormView.as_view(), name='signup'),
    path('password-renitialise/', TemplateView.as_view(template_name='accounts/fogort-password.html'), name='password-renitialise'),
    path('profile/<int:id>/', views.ProfileFormView.as_view(), name='profile-detail'),
    path('list/',views.UserListView.as_view(), name='users'),
    # path('list/', TemplateView.as_view(template_name='accounts/list.html'), name='list-user')
]
