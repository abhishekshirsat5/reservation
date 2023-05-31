from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('auth/', views.loginPage, name="auth"),
    path('logo/', views.outuser, name="logo"),
    path('book/', views.bookNow, name="book"),
    path('confirm/', views.confirmPage, name="confirm"),
    path('chenageway/', views.chenageway, name="chenageway"),
    path('cancelOrder/', views.cancelOrder, name="cancelOrder"),
    path('pay/', views.payment_complete, name="pay"),
    path('renderNow/', views.renderConfirm, name="redirectpage"),
]
