from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path(
        'legal_mentions/',
        views.LegalMentionsView.as_view(),
        name='legal_mentions'
    ),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profil/', views.ProfilView.as_view(), name='profil'),
]
