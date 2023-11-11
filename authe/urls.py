from django.urls import path
from authe.views import *
app_name = 'authe'

urlpatterns = [
    path(route='register/', view=register_view, name="register"),
    path(route='register_admin/', view=register_admin_view,
         name="register_admin"),
    path(route='login/', view=login_view, name="login"),
    path(route='otp/', view=otp_view, name="otp"),
    path(route='home/', view=home_view, name="home"),
    path(route='admin_home/', view=admin_home_view, name="admin_home"),
    path(route='logout/', view=logout_view, name="logout"),
]
