from django.shortcuts import render
from django.http import HttpResponse


def profile_view(request, user_id: int = None):
    stub_response_str = "There will be user`s profile"
    if user_id:
        stub_response_str += f' with id = {user_id}'

    return HttpResponse(stub_response_str)