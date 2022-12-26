
from django.urls import path
from goods import views



urlpatterns = [
    path('api/category/', views.create_category),
    path('api/category/<int:pk>/', views.detail_category),
    path('api/firm/', views.create_firm),
    path('api/firm/<int:pk>/', views.detail_firm),
    path('api/good/', views.create_good),
    path('api/good/<int:pk>/', views.detail_good),
]
