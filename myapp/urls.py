from django.urls import path
from .views import HomeView, PostDetailView
#s
from rest_framework_swagger.views import get_swagger_view


#schema_view = get_swagger_view(title='Pastebin API')


app_name = 'myapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    #path('endpoint/', views.YourView.as_view(), name='your-endpoint'),
    #path('swagger/', schema_view, name = 'sagger'),
]


