from django.urls import path, include
from eventer_app.events.views import dashboard_page, create_page, event_details_page, edit_event_page, delete_event_page

urlpatterns = [
    path('dashboard/', dashboard_page, name='dashboard'),
    path('create/', create_page, name='create_page'),
    path('details/<int:pk>/', event_details_page, name='details_page'),
    path('edit/<int:pk>/', edit_event_page, name='edit_page'),
    path('delete/<int:pk>/', delete_event_page, name='delete_page')
]