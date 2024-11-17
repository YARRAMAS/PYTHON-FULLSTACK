from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home, name="home"),
    path('signin/',views.signin, name="signin"),
    path('logout/', views.logout, name='logout'),
    path('forgot/', views.forgot,name="forgot"),
    path('admin/',views.admin, name='admin'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name="search"),
    path('cancel/',views.cancel, name="cancel"),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('search_employee/', views.search_employee, name='search_employee'),
    path('edit_employee/<str:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<str:employee_id>/', views.delete_employee, name='delete_employee'),
    path('tabs/',views.tabs,name="tabs"),
    path('menu/',views.menu,name='menu'),
    path('auto/',views.auto,name='auto'),
    path('collapsible/',views.collapsible,name='collapsible'),
    path('images/',views.images,name='images'),
    path('slider/',views.slider,name='slider'),
    path('tooltips/',views.tooltips,name='tooltips'),
    path('popups/',views.popups,name='popups'),
    path('links/',views.links,name='links'),
    path('cssprops/',views.cssprops,name='cssprops'),
    path('iframes',views.iframes,name='iframes'),
]