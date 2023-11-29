from django.shortcuts import render
from django.http import HttpResponse


def index(request, login="Noname", folder="Nofolder", folder_num=0):
    return HttpResponse(f'Login: {login}, folder: {folder}, folder num: {folder_num}',
                        headers={'SecretCode': '1254478'})
