from django.urls import path, include
from eventer_app.shared.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
]