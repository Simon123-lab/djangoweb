from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage),
    path('order',views.orderpromotion),
    path('login',views.workerlogin),
    path('reg',views.registration),
    path('token',views.deliver_token),
    path('verified',views.token_success),
    path('subscribe',views.packages),
    path('verify/<auth_token>',views.verify),
    path('error',views.error),
    path('dashboard',views.user_profile),
    path('tasks',views.user_tasks),
    path('logout',views.logout),
    path('connect',views.client_connect),
    path('herologin',views.client_login),
    path('panel',views.hero_panel)
]
