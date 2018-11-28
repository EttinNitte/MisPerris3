from django.http import HttpResponse
import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    response = requests.get('http://api.ipstack.com/200.14.248.139?access_key=ed45289eb6aa84378442d6c312320945')
    data = response.json()
    return render(request,'index.html',{'latitud': data['latitude'],'longitud': data['longitude'],'ciudad': data['city'],'region': data['region_code'],'ip': data['ip'], 'pais': data['country_name'] })