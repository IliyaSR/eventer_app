from django.urls import path, include
from eventer_app.profiles.views import profile_details_page, edit_profile_page, \
    delete_profile_page, create_profile_page

urlpatterns = [
    path('create/', create_profile_page, name='create_profile'),
    path('details/', profile_details_page, name='details_profile'),
    path('edit/', edit_profile_page, name='edit_profile'),
    path('delete/', delete_profile_page, name='delete_profile')
]
