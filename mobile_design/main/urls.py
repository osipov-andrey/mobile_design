from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:app_name>/', views.AppPage.as_view(), name='app_page'),
    path('<str:app_name>/<int:pk>/', views.ScreenDetail.as_view(), name='screen_detail'),

]
