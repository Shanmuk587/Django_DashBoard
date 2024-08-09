from django.urls import path
from . import views

urlpatterns = [
    path('panel-dashboard/', views.panel_dashboard_view, name='panel_dashboard'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('panel-chatbot/', views.panel_dashboard_view, name='panel_chatbot'),
    path('chatbot/', views.chatbot, name='chatbot')
]
