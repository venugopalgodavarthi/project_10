from django.urls import path
from authe.views import register_view, login_view, home_view, logout_view, otp_view
app_name = 'authe'

urlpatterns = [
    path(route='register/', view=register_view, name="register"),
    path(route='login/', view=login_view, name="login"),
    path(route='otp/', view=otp_view, name="otp"),
    path(route='home/', view=home_view, name="home"),
    path(route='logout/', view=logout_view, name="logout"),
]
