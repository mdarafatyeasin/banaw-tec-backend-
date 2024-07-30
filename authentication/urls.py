from django.urls import path
from . import views


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('registration', views.userRegistration.as_view(), name='user-registration'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/<int:id>/<token>', views.UserLogOut, name='logout'),
]

