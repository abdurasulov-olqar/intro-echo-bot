import requests
import time

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
    # url for sending message
    url_for_sending_msg = BASE_URL + "sendSticker"
    # qurey parameters for resquest
    payload = {
        "chat_id": chat_id,
        "sticker": sticker
    }
    # send message
    response = requests.get(url_for_sending_msg, params=payload)
    return response.status_code

def sendContact(chat_id, phone_number, first_name, last_name = ''):
    # url for sending message
    url_for_sending_msg = BASE_URL + "sendContact"
    # qurey parameters for resquest
    payload = {
        "chat_id": chat_id,
        "phone_number": phone_number,
        "first_name": first_name,
        "last_name": last_name
    }
    # send message
    response = requests.get(url_for_sending_msg, params=payload)
    return response.status_code


def main():
    # for last update id
    last_update_id = -1
    while True:
        # current update
        curr_update = get_last_update()
        # current update id
        curr_update_id = curr_update['update_id']
        # check new update
        if last_update_id != curr_update_id:
            last_message = curr_update['message']
            # get data for send message
            chat_id = last_message['chat']['id']
            text = last_message.get('text')
            if text:
                # send message
                sendMessage(chat_id, text)
            sticker = last_message.get('sticker')
            if sticker:
                # send Sticker
                sendSticker(chat_id, sticker)
            contact = last_message.get('contact')
            if contact:
                # send Contact
                phone_number = contact['phone_number']
                first_name = contact['first_name']
                last_nam = contact.get('last_name')
                last_name = ''
                if last_nam:
                    last_name = contact['last_name'] 
                sendContact(chat_id, phone_number, first_name, last_name)
            last_update_id = curr_update_id
        
        time.sleep(1)


main()