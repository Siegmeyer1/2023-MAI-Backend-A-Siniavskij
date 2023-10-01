from django.shortcuts import render
from django.http import HttpResponse


def chat_list_view(request):
    return HttpResponse("There will be list of user`s chats")

def chat_view(request, chat_id: int):
    return HttpResponse(f"There will be chat with id = {chat_id}")
