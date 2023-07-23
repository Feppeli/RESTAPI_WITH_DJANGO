from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.


def index(request):
    return HttpResponse("Hello world. You're at the polls index.")

# def postUser(request):
#     return teste;


def post_user(request):
    newUser = User()
    newUser.name = request.post('name')
    newUser.save()


def get_message(request):
    return HttpResponse('teste de rota')
