from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('my-purchases/', views.my_purchases, name='my_purchases'),
    path('specialists/', views.specialists, name='specialists'),
    path('specialist/<int:pk>/', views.specialist_detail, name='specialist_detail'),
    path('specialist/<int:pk>/book/', views.book_consultation, name='book_consultation'),
    path('booking/<int:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('meal-plans/', views.meal_plans, name='meal_plans'),
    path('meal-plan/<int:pk>/purchase/', views.purchase_meal_plan, name='purchase_meal_plan'),
    path('purchase/<int:purchase_id>/confirmation/', views.purchase_confirmation, name='purchase_confirmation'),
]