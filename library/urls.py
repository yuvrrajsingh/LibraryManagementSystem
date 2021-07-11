from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm
urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:pk>', views.book_detail.as_view(), name='book_detail'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='library/login.html', authentication_form=LoginForm), name='login'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='library/change_pass.html', form_class=MyPasswordChangeForm, success_url='/changepassworddone/'), name='changepass'),
    path('changepassworddone/', auth_views.PasswordChangeDoneView.as_view(template_name='library/changepassworddone.html'), name='changepassworddone'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('issue/<int:pk>', views.book_issue, name='issue'),
    path('return/<int:pk>/<int:id>', views.book_return, name='return'),
]
