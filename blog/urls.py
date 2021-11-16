from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index_View, name='index'),
    path('add/', views.createArticle, name='add'),
    path('admin/', views.Admin_View, name='admin'),
    path('<int:id>/', views.singleArticle, name='single'),
    path('edit/<int:pk>/', views.updateArticle, name='edit'),
    path('delete/<int:pk>', views.deleteArticle, name='delete'),
    path('register/', views.User_Register, name='register'),
    path('login/', views.Login_User, name='login'),
    path('logout/', views.Logout_User, name='logout'),
    path('reply/<int:pk>/', views.viewReplies, name='reply')
]
