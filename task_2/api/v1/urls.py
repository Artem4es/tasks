from django.urls import path

from .views import ProductView

app_name = 'api_v1'


urlpatterns = [
    path('products/', ProductView.as_view()),
]
