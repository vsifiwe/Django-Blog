from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('admin/', views.AdminView.as_view(), name='admin'),
    # path('<int:pk>/', views.SingleView.as_view(), name='single'),
    path('<int:id>/', views.singleArticle, name='single'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>', views.DeleteArticleView.as_view(), name='delete'),
    path('<int:pk>/comment', views.AddComment.as_view(), name='comment')
]
