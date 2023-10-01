from django.urls import path, include

urlpatterns = [
    path('chats/', include('chats.urls')),
    path('users/', include('users.urls')),
]