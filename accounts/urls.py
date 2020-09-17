from django.urls import path

from accounts import views

urlpatterns = [
    path('signin/', views.MyLoginView.as_view(), name="signin"),
    path('signout/', views.MyLogoutView.as_view(), name="signout"),
    path('index/', views.IndexView.as_view(), name='index'),
    path('signup/', views.UserCreateView.as_view(), name="signup"),
]