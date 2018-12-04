# -*- coding: utf-8 -*-


import requests
import json
import os

GRAPH_URL = "https://graph.facebook.com/v2.6"

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']




def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text.encode('utf-8')}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_image(id, img_url):
    response_img = json.dumps({"recipient": {"id":id},"message": {
            "attachment":{
                "type": "image",
                "payload": {
                    "url": img_url
                }
             }
         }
     })
    post_message_url = GRAPH_URL + "/me/messages?access_token="+ ACCESS_TOKEN
    requests.post(post_message_url,headers={"Content-Type": "application/json"},data=response_img)
    print(post_message_url)


def template_message(id,title,img_url,subtitle,data):
    response_template = json.dumps({"recipient": {"id":id},"message": {
        "attachment":{
            "type":"template",
            "payload": {
                "template_type": "generic",
                "elements":[
                    {
                        "title": title,
                        "image_url": img_url,
                        "subtitle": subtitle,
                        "buttons": data
                    }
                 ]
             }
         }
     }
 })
    post_message_url = GRAPH_URL + "/me/messages?access_token="+ ACCESS_TOKEN
    requests.post(post_message_url,headers={"Content-Type": "application/json"},data=response_template)
   
          
def quick_reply_message(id,text,quick_replies):
    response_fast = json.dumps({"recipient":{"id": id}, "message":{
        "text":text,
        "quick_replies": quick_replies
        }})
    post_message_url = GRAPH_URL + "/me/messages?access_token="+ ACCESS_TOKEN
    requests.post(post_message_url,headers={"Content-Type": "application/json"},data=response_fast)
   


def send_button_message(id, text, buttons):
    pass

