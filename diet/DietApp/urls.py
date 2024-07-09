from django.urls import path
from . import views


app_name = 'DietApp'

urlpatterns = [
    path('', views.main, name="main"),
    
    path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name='register'),
    
    path('predict/', views.predict, name='predict'),
    path('viewpredictions/', views.viewpredictions, name='viewpredictions'),
    path('view_meals/', views.view_meals, name='view_meals'),
    path('recommended_meal/', views.recommended_meal, name='recommended_meal'),
    path('about/', views.about, name="about"),
    
]