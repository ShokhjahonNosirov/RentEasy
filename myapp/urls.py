from django.urls import path
from .views import HomeView, PostDetailView

app_name = 'myapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
]