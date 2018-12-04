# -*- coding: utf-8 -*-

from bottle import route, run, request, abort, static_file
import time
from fsm import TocMachine
from utils import send_text_message,send_image,template_message,quick_reply_message


VERIFY_TOKEN = "1234567890"
timeStamp = 0
sender = 0
recipient = 0
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'ABC',
        'Act',
        'Unhappy',
        'Out',
        'FEcolor',
        'FEmove',
        'Mumi',
        'Hero',
        'Hero2',
        'FEbody',
        'FEskill',
        'FEimage',
        'selectSong',
        'Song',
        'rightSong',
        'wrongSong',
        'continueSong',
        'Ptt',
        'PttNum',
        'pttPush',
        'pttWord'

        
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
            
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'ABC',
            'conditions': 'isABC'
        },

        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'Act',
            'conditions' : 'pretty_girl'
    
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'Out',
            'conditions' : 'fat_loser'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'Act',
            'dest': 'FEcolor',
            'conditions' : 'isFE'
           
            
        },
  
        {
            'trigger': 'advance',
            'source': 'Act',
            'dest': 'selectSong',
            'conditions' : 'isSong'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'Act',
            'dest': 'Ptt',
            'conditions' : 'isPtt'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'Act',
            'dest': 'Mumi',
            'conditions' : 'not_empty'
           
            
        },

        {
            'trigger': 'advance',
            'source': 'selectSong',
            'dest': 'Song',
            'conditions' : 'validSex'
           
            
        },
    
        {
            'trigger': 'advance',
            'source': 'continueSong',
            'dest': 'Act',
            'conditions' : 'stopPlay'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'Ptt',
            'dest': 'PttNum',
            'conditions' : 'validBoard'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'PttNum',
            'dest': 'pttPush',
            'conditions' : 'validAmount'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'Ptt',
            'dest': 'Mumi',
            'conditions' : 'not_empty'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'PttNum',
            'dest': 'Mumi',
            'conditions' : 'not_empty'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'pttPush',
            'dest': 'pttWord',
            'conditions' : 'validPush'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'pttPush',
            'dest': 'Mumi',
            'conditions' : 'not_empty'
           
            
        },

        {
            'trigger': 'advance',
            'source': 'pttWord',
            'dest': 'Ptt',
            'conditions' : 'continue_ask'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'pttWord',
            'dest': 'Act',
            'conditions' : 'stopPlay'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'pttWord',
            'dest': 'Mumi',
            'conditions' : 'not_empty'
           
            
        },

        {
            'trigger': 'advance',
            'source': 'FEcolor',
            'dest': 'FEmove',
            'conditions' : 'validWeapon'
           
        },
        {
            'trigger': 'advance',
            'source': 'selectSong',
            'dest': 'Mumi',
            'conditions' : 'not_empty'
           
        },
        {
            'trigger': 'advance',
            'source': 'Song',
            'dest': 'rightSong',
            'conditions' : 'isRight'
           
        },
        {
            'trigger': 'advance',
            'source': 'Song',
            'dest': 'wrongSong',
            'conditions' : 'not_empty'
           
        },

        {
            'trigger': 'advance',
            'source': ['rightSong','wrongSong'],
            'dest': 'continueSong'
            
           
        },

        {
            'trigger': 'advance',
            'source': 'continueSong',
            'dest': 'Song',
            'conditions' : 'continue_ask'
           
        },
        {
            'trigger': 'advance',
            'source': 'continueSong',
            'dest': 'Mumi',
            'conditions' : 'not_empty'
           
        },


        {
            'trigger': 'advance',
            'source': 'FEmove',
            'dest': 'Hero',
            'conditions' : 'validMove'
           
        },
        {
            'trigger': 'advance',
            'source': 'FEcolor',
            'dest': 'Mumi',
            'conditions' : 'not_empty'
           
        },
        {
            'trigger': 'advance',
            'source': 'FEmove',
            'dest': 'Mumi',
            'conditions' : 'not_empty'
           
        },

        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'Unhappy',
            'conditions' : 'not_empty'
           
            
        },

        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'Act',
            'conditions' : 'feel_happy'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'Unhappy',
            'conditions' : 'not_empty'
           
            
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions' : 'not_empty'         
            
        },
        {
            'trigger': 'go_back',
            'source':  'Hero',
            'dest': 'FEcolor'
        },
        {
            'trigger': 'advance',
            'source':  'Hero',
            'dest': 'Hero2',
            'conditions' : 'validName'
        },
        {
            'trigger': 'advance',
            'source':  'Hero',
            'dest': 'Mumi',
            'conditions' : 'not_empty'
        },

        {
            'trigger': 'advance',
            'source':  'Hero2',
            'dest': 'FEimage',
            'conditions' : 'isImage'
        },

        {
            'trigger': 'advance',
            'source':  'Hero2',
            'dest': 'FEskill',
            'conditions' : 'isSkill'
        },

        {
            'trigger': 'advance',
            'source':  'Hero2',
            'dest': 'FEbody',
            'conditions' : 'isBody'
        },
        {
            'trigger': 'advance',
            'source':  'Hero2',
            'dest': 'NOP',
            'conditions' : 'not_empty'
        },

        {
            'trigger': 'advance',
            'source':  ['FEbody','FEskill','FEimage'],
            'dest': 'Hero2',
            'conditions' : 'continue_ask'
        },

        {
            'trigger': 'advance',
            'source':  ['FEbody','FEskill','FEimage'],
            'dest': 'FEcolor',
            'conditions' : 'other_people'
        },

        {
            'trigger': 'advance',
            'source':  ['FEbody','FEskill','FEimage'],
            'dest': 'Mumi',
            'conditions' : 'not_empty'
        },


        {
            'trigger': 'go_back',
            'source': [
                'ABC',
                'state3',
                'Unhappy',
                'Out',
                'Mumi',
                'NOP'
             ],
            'dest': 'user'
        }        
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")
    
    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    global timeStamp
    global sender
    global recipient
    now  = int(time.time())
    
  #  if(now - timeStamp < 3):
     #   return 'OK'
       
   #     print('Repeated Message',str(timeStamp),str(now))
    #    return 'OK'
    body = request.json
    try:    
        sender_id = body['entry'][0]['messaging'][0]['sender']['id']
        re_id = body['entry'][0]['messaging'][0]['recipient']['id']
        
        if recipient and sender_id == recipient:
            print("System message")
            return 'OK'
        print(body)
        recipient = re_id
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
    except Exception as e:
        print(e)
    print(machine.state)
    timeStamp = int(time.time())
    print("Now",str(timeStamp))    
    return 'OK'
  #  if body['object'] == "page":
   #     event = body['entry'][0]['messaging'][0]
    #    machine.advance(event)
     #   return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=8000, debug=True, reloader=True)
    
