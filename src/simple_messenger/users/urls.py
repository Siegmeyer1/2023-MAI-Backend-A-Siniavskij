from users.views import profile_view
from django.urls import path


urlpatterns = [
    path('profile/', profile_view, name='profile_view'),
    path('profile/<int:user_id>', profile_view, name='profile_view')
]