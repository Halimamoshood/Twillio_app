import json
import urllib.request
from random import randint
from flask import flash, render_template

import requests
from twilio.rest import Client


def log_msg(log, msg):

    with open(log, '+a') as logged:
        logged.write(msg)
    logged.close()


def weather():

    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}
    headers = {
        "X-RapidAPI-Key": "0a109dce92msh070cc32fb93c003p1e4e8djsnef8cf195fed1",
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


def harryPorter():

    url = urllib.request.Request('http://hp-api.herokuapp.com/api/characters', headers={'User-Agent': 'Mozilla/5.0'})
    request = urllib.request.urlopen(url)
    response_1 = json.loads(request.read())

    return response_1[randint(0,402)]


def space():

    url = urllib.request.Request('http://api.open-notify.org/astros.json', headers={'User-Agent': 'Mozilla/5.0'})

    request = urllib.request.urlopen(url)
    response_1 = json.loads(request.read())
    return response_1

# print(weather())

def message_org():

    return f'''
        weather today:

        {weather()}

     brought to you by {harryPorter()["name"]} from Magic land and {space()["people"][randint(0,9)]["name"]} from Space'''

def send_sms():
    account_sid = 'AC5e64d8e72525dc8b89b2f28ad22fd340' 
    auth_token = 'cd0abf0ef610c63ea4992fdf4739a56f' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create(
        body=f'{message_org()}',
        to='+2348075534891',
        from_= '+18312563901'
        ) 

    log_msg('log.txt', message_org())

    if message.sid:
        flash("your message was sent successfuly", 'info')  
    else:
        flash("your message was not sent!!", 'error')  
    
    return render_template('success.html')

def home():
    return render_template('index.html')

    # flash("your message was sent successfuly", 'info')  
    # flash("your message was not sent!!", 'error')  
