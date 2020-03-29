from django.urls import path, re_path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<app_name>.+)/(?P<patterns>patterns)/$', views.AppPage.as_view(), name='app_page_patterns'),
    re_path(r'^(?P<app_name>.+)/(?P<elements>elements)/$', views.AppPage.as_view(), name='app_page_elements'),
    path('<str:app_name>/', views.AppPage.as_view(), name='app_page'),
    #path('<str:app_name>/elements/', views.AppPageElements.as_view(), name='app_page_elements'), # должно быть всплывающее меню
    path('<str:app_name>/<int:pk>/', views.ScreenDetail.as_view(), name='screen_detail'),

]
