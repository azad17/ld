from django.urls import path
from . import views

urlpatterns = [
    path("signup",views.SignupView.as_view(),name='signup'),
    path("signin",views.SigninView.as_view(),name="signin"),
    path("signout",views.SignoutView.as_view(),name="signout"),
    path('user-profile',views.UserProfile.as_view(),name='user-profile')
]