from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

name = 'blogs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='product_list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/edit/', views.modify, name='modify'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
