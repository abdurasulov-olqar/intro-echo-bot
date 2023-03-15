import requests


TOKEN = '5591155154:AAHn0llNadmGCykPsdpkfc5OXcv54S0MQyc'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'

def get_last_update():
    # make url for getupdates
    url_for_getupdates = BASE_URL + "getUpdates"
    # meke request
    response = requests.get(url_for_getupdates)
    # check rsponse status
    if response.status_code == 200:
        # get data from response as dict
        data = response.json()
        # get result
        result = data['result']
        # get last update
        last_update = result[-1]
        return last_update
    return False

def sendMessage(chat_id, text):
    # url for sending message
    url_for_sending_msg = BASE_URL + "sendMessage"
    # qurey parameters for resquest
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    # send message
    response = requests.get(url_for_sending_msg, params=payload)
    return response.status_code

def sendSticker(chat_id, sticker):
    # url for sending sticker
    url_for_sending_msg = BASE_URL + "sendSticker"
    # qurey parameters for resquest
    payload = {
        "chat_id": chat_id,
        "sticker": sticker
    }
    # send sticker
    response = requests.get(url_for_sending_msg, params=payload)
    return response.status_code

def sendContact(chat_id, phone_number, first_name, last_name = ''):
    # url for sending contact
    url_for_sending_msg = BASE_URL + "sendContact"
    # qurey parameters for resquest
    payload = {
        "chat_id": chat_id,
        "phone_number": phone_number,
        "first_name": first_name,
        "last_name": last_name
    }
    # send contact
    response = requests.get(url_for_sending_msg, params=payload)
    return response.status_code

def sendLocation(chat_id, latitude, longitude):
    # url for sending location
    url_for_sending_msg = BASE_URL + "sendLocation"
    # qurey parameters for resquest
    payload = {
        "chat_id": chat_id,
        "latitude": latitude,
        "longitude": longitude
        
    }
    # send location
    response = requests.get(url_for_sending_msg, params=payload)
    return response.status_code

def sendPhoto(chat_id, photo):
    # url for sending photo
    url_for_sending_msg = BASE_URL + "sendPhoto"
    # qurey parameters for resquest
    payload = {
        "chat_id": chat_id,
        "photo": photo, 
    }
    # send photo
    response = requests.get(url_for_sending_msg, params=payload)
    return response.status_code

def sendAnimation(chat_id, animation):
    # url for sending animation
    url_for_sending_msg = BASE_URL + "sendAnimation"
    # qurey parameters for resquest
    payload = {
        "chat_id": chat_id,
        "animation": animation, 
    }
    # send Animation
    response = requests.get(url_for_sending_msg, params=payload)
    return response.status_code

def sendAudio(chat_id, audio):
    # url for sending audio
    url_for_sending_msg = BASE_URL + "sendAudio"
    # qurey parameters for resquest
    payload = {
        "chat_id": chat_id,
        "audio": audio, 
    }
    # send Animation
    response = requests.get(url_for_sending_msg, params=payload)
    return response.status_code

def sendDocument(chat_id, document):
    # url for sending document
    url_for_sending_msg = BASE_URL + "sendDocument"
    # qurey parameters for resquest
    payload = {
        "chat_id": chat_id,
        "document": document, 
    }
    # send Animation
    response = requests.get(url_for_sending_msg, params=payload)
    return response.status_code
