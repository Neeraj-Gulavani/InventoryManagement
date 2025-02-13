from django.urls import path
from . import views
app_name = 'login'
urlpatterns = [
    path('',views.index,name="index"),
    path('logout',views.logout_view,name="logout_view")
    #path('login',views.login_request,name="loginpage")
]