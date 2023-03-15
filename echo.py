import time
from handlers import (
    get_last_update,
    sendMessage, 
    sendSticker,
    sendContact,
    sendLocation,
    sendPhoto,
    sendAnimation,
    sendAudio,
    sendDocument
)

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

            location = last_message.get('location')
            if location:
                # send Location
                latitude = location['latitude']
                longitude = location['longitude']
                sendLocation(chat_id, latitude, longitude)
            
            photo = last_message.get('photo')
            if photo:
                # send photo
                photo = photo[-1]['file_id']
                
                sendPhoto(chat_id, photo)

            animation = last_message.get('animation')
            if animation:
                # send animation
                animation = animation['file_id']
                sendAnimation(chat_id, animation)

            audio = last_message.get('audio')
            if audio:
                # send audio
                audio = audio['file_id']
                sendAudio(chat_id, audio)

            document = last_message.get('document')
            if document:
                # send document 
                document = document['file_id']
                print(document)
                sendDocument(chat_id, document)


            last_update_id = curr_update_id
        
        time.sleep(1)


main()