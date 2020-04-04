from django.urls import path, re_path
from . import views

app_name = 'accounts'
urlpatterns = [

    path('register/done/', views.RegisterDoneView.as_view(), name='register_done'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('password/change/', views.AccountsPasswordChangeView.as_view(), name='password_change'),
    path('logout/', views.AccountsLogoutView.as_view(), name='logout'),
    path('login/', views.AccountsLoginView.as_view(), name='login'),
    path('profile/delete/', views.DeleteUserView.as_view(), name='profile_delete'),
    path('profile/change/', views.ChangeUserInfoView.as_view(), name='profile_change'),

    # path('profile/change/<int:pk>/', views.profile_change, name='profile_change'),
    # path('profile/delete/<int:pk>/', views.profile_delete, name='profile_delete'),
    # path('profile/add/', views.profile_add, name='profile_bb_add'),
    # path('profile/<int:rubric_pk>/<int:pk>/', views.profile_detail, name='profile_detail'),
    # path('profile/', views.profile, name='profile'),  # по этому пути django по умолчанию перенаправляет после входа


]
