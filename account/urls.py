
from django.urls import path
from account.views.loginmethod import LoginMethod
from account.views.resigter import Register
from account.views.LogoutMethod import LogoutMethod

urlpatterns = [
    path('signin/', LoginMethod.as_view(), name="signin"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', LogoutMethod.as_view(), name = "logout")
]
