from chats.views import chat_list_view, chat_view
from django.urls import path


urlpatterns = [
    path('', chat_list_view, name='chat_list_view'),
    path('<int:chat_id>/', chat_view, name='chat_view'),
]