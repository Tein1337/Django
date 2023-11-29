from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']

    return HttpResponse(f'host: {host} <br> browser: {user_agent} <br> ip: {ip} <br>',
                        headers={'SecretCode': '1254478'})


def error(request):
    return HttpResponse(f'К сожелению произошла ошибка', status=400, reason='Error')