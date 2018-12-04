# -*- coding: utf-8 -*-
from transitions.extensions import GraphMachine


from utils import send_text_message,send_image,template_message,quick_reply_message
import random
import requests
import re
from bs4 import BeautifulSoup as soup
import nltk
from nltk.corpus import wordnet
nonsense = [u'嗯哼？',u'你的意思是？',u'你說什麼？',u'我不懂你',u'你就試著取悅我吧',u'總該先打聲招呼吧',u'你在想什麼？',u'為什麼要這樣說？',u'我認為我們應該談點別的',u'全世界的人都在學中國話',u'你想表達什麼？']

weapon = {u'劍':'120894',u'槍':'120886',u'斧':'120896',u'弓':'120902',u'藍弓':'230172'
,u'綠弓':'215799',u'暗器':'120898',u'赤暗器':'236508',u'藍暗器':'231539',u'綠暗器':'231540'
,u'杖':'120903',u'紅法':'120892',u'藍法':'174371',u'綠法':'174372',u'無龍':'210813',u'紅龍'
  :'120893',u'藍龍':'174375',u'綠龍':'174374'
          }
move = {u'步行':u'歩行',u'騎兵':u'騎馬',u'重甲':u'重装',u'飛行':u'飛行'}
sex = True
url='https://game8.jp/fe-heroes/'
conditon = ''
lang = {}
link = ''
songName = ''
board = ''
amount = 1
threshold = 1
word = ''
boy = ['twh102520','twh100012','twh100951','twh104616','twh105661','twh105350','twh108483','twh100294','twh102372']
girl = ['twh100163','twh100593','twh100095','twh102453','twh105079','twh100954','twh104279','twh104613','twh100090']
    
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.encode('utf-8') == '你好'
        return False
    
    def not_empty(self, event):
        if event.get("message"):
            text = event['message']['text']
            return len(text) >= 1
        return False

    def pretty_girl(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == u'正妹'


        return False
   
    def Never(self,event):  
        return False
     

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == u'你是大帥哥'
        return False
    def isABC(self, event):
        global word
        if event.get("message"):
            text = event['message']['text']
            if text.encode('utf-8').isalpha():
                syn = wordnet.synsets(text)
                if len(syn) > 0:
                    word = text
                    return True
        return False
 
    def feel_happy(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == u'求您疼我'
        return False
 
    def isBody(self, event):
     
        if event.get("postback"):
            text = event['postback']['title']
            return text == u'英雄標準體質'
        elif event.get("message"):
            text = event['message']['text']
            return text ==u'英雄標準體質'
 
        return False

    def isSkill(self, event):
     
        if event.get("postback"):
            text = event['postback']['title']
            return text == u'擁有技能'
        elif event.get("message"):
            text = event['message']['text']
            return text ==u'擁有技能'
 
        return False
    def isImage(self, event):
     
        if event.get("postback"):
            text = event['postback']['title']
            return text == u'看照片'
        elif event.get("message"):
            text = event['message']['text']
            return text ==u'看照片'
 
        return False

    def continue_ask(self, event):
        if event.get("message"):
            text = event['message']['text']
            
            return (text == u'好' or text == u'是' or text == u'對')
        return False
    
    def other_people(self, event):
        if event.get("message"):
            text = event['message']['text']
            
            return (text == u'換別人' or text == u'想換一個' or text == u'來點別的' or text == '否')
        return False

    def stopPlay(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text == u'不要'
        return False

    def fat_loser(self, event):
        if event.get("message"):
            text = event['message']['text']
            
            return text == u'資訊系肥宅'
        return False
    def isFE(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            return text == u'查詢聖火手遊資料'
        elif event.get("message"):
            text = event['message']['text']
            return text ==u'查詢聖火手遊資料'

        return False

    def isSong(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            return text == u'玩猜歌遊戲'
        elif event.get("message"):
            text = event['message']['text']
            return text ==u'玩猜歌遊戲'
        return False
    def isPtt(self, event):
        if event.get("postback"):
            text = event['postback']['title']
            return text == u'看ptt的文章'
        elif event.get("message"):
            text = event['message']['text']
            return text ==u'看ptt的文章'
        return False
  
    def validWeapon(self, event):
        global url
        if event.get("message"):
            text = event['message']['text']
            if weapon.has_key(text):
                url='https://game8.jp/fe-heroes/' + weapon[text]
                
                return True
            
    
        return False
    def validSex(self, event):
        global sex
        if event.get("message"):
            text = event['message']['text']
            if text == u'男歌手':
                sex = True
                return True
            elif text == u'女歌手':
                sex = False
                return True
            
    
        return False

  
    def validMove(self, event):
        global condition
        if event.get("message"):
            text = event['message']['text']
            if move.has_key(text):
                condition = move[text]
                return True
            
        return False
    def validAmount(self, event):
        global amount
        if event.get("message"):
            text = event['message']['text']
            try:
                
                amount = int(text)
                if(amount <= 0):
                    return False
                return True
            except:
                return False
        return False

    def validBoard(self, event):
        global board
        if event.get("message"):
            text = event['message']['text']
            dev = "https://www.ptt.cc/bbs/" + text + "/index.html"
            page = requests.get(dev).text
            htm = soup(page,'html.parser')
            links = htm.select('a.wide')
            if(len(links) >= 1):
                board = text
                return True
                
            else:
                return False
          
        return False


    def validPush(self, event):
        global threshold
        if event.get("message"):
            text = event['message']['text']
            try:
                
                threshold = int(text)
                if(threshold <= 0):
                    return False
                return True
            except:
                return False
        return False

    def validName(self, event):
        global lang
        global link
        if event.get("message"):
            text = event['message']['text']
            if lang.has_key(text):
                link = lang[text]
                print(link)
                return True
            
        return False

    def isRight(self, event):
        global songName
        if event.get("message"):
            text = event['message']['text']
            if songName == text:
                return True
            
        return False



    def on_enter_state1(self, event):
        print("請問你是誰？")

        sender_id = event['sender']['id']
        data = [
                 {
                     "content_type": "text",
                     "title": "正妹",
                     "payload" : "正妹"
                 },
                 {
                     "content_type": "text",
                     "title": "資訊系肥宅",
                     "payload" : "資訊系肥宅"
                 }
             ]
        quick_reply_message(id = sender_id,text = "請問你是誰？",quick_replies=data)
               
        
    
    def on_enter_state2(self, event):
        print("你想做什麼？")
         
        sender_id = event['sender']['id']
        send_text_message(sender_id,u'你就試著取悅我吧')
              
    def on_enter_ABC(self, event):
        global word       
        sender_id = event['sender']['id']
        syn = wordnet.synsets(word)
        s = syn[0]
        send_text_message(sender_id,(s.definition()).capitalize())
        for e in s.examples():
            send_text_message(sender_id,e.capitalize())

        self.go_back()
    def on_enter_state3(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, random.choice(nonsense))
        self.go_back()       
    def on_enter_rightSong(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,u'你答對了！')
        self.advance(event) 
    def on_enter_wrongSong(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,u'你答錯了，應該是' + songName)
        self.advance(event)

    def on_enter_Unhappy(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,u'我看還是算了吧')
        self.go_back() 
    def on_enter_Out(self,event):
        sender_id = event['sender']['id']
        send_image(sender_id,'https://i.imgur.com/K29GlOK.jpg')
        self.go_back() 
    def on_enter_Mumi(self,event):
        sender_id = event['sender']['id']
        send_image(sender_id,'https://i.imgur.com/1O6ugQR.jpg')
        self.go_back() 
    def on_enter_Ptt(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,u'請問要瀏覽那一個看板？')
    def on_enter_PttNum(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,u'請問要看幾篇文章？')
    def on_enter_pttPush(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,u'請問要搜尋幾推以上的文章？')
 
    def on_enter_pttWord(self,event):
        global amount
        global threshold
        global board
        sender_id = event['sender']['id']
        url = "https://www.ptt.cc/bbs/" + board + "/index.html"
        page = requests.get(url).text
        htm = soup(page,'html.parser')
        links = htm.select('a.wide')
        link = links[1]
        txt = link.get('href')
        txt = txt.split("index")[1][:-5]
        nextpage = int(txt)
        val = 0;
       # threshold = 30;
       # amount = 10;
        send_text_message(sender_id,u'你要' + str(amount) + u'篇')      
        while(val < amount):
            page = requests.get(url).text
            htm = soup(page,'html.parser')
            items = htm.select("div.nrec > span")
            i = htm.select("div.title > a")
            count = 0
            for item in items:
                if items[count].text.find("X") != -1:
                   count = count + 1;
                   continue;
                if val >= amount:
                    break
                if(items[count].text == u"爆" or int(items[count].text) > threshold):
                    send_text_message(sender_id,items[count].text + ' ' + i[count].text + '\n' + 'https://www.ptt.cc' + i[count].get('href'))
                    val = val + 1
                count = count + 1
            nextpage = nextpage - 1;
            url = "https://www.ptt.cc/bbs/" + board + "/index" + str(nextpage) + ".html"
       
        data = [
             {
                 "content_type": "text",
                 "title": "好",
                 "payload" : "好"
             },
             {
                 "content_type": "text",
                 "title": "不要",
                 "payload" : "不要"
             }
         ]
        quick_reply_message(id = sender_id,text = "要繼續搜尋嗎？",quick_replies=data)
             

    def on_enter_Act(self,event):
        print('Enter State 4')
        sender_id = event['sender']['id']
        data = [
                {
                    "type" : "postback",
                    "title" : u"查詢聖火手遊資料",
                    "payload": u"查詢聖火手遊資料"
                },
                {  
                    "type" : "postback",
                    "title" : "玩猜歌遊戲",
                    "payload": "玩猜歌遊戲"
                },
                {  
                    "type" : "postback",
                    "title" : "看ptt的文章",
                    "payload": "看ptt的文章"
                } 
             ]
        template_message(
                   id = sender_id,
                    title="請盡情為所欲為",
                    img_url="https://i.imgur.com/xQF5dZT.jpg",
                    subtitle="相信你的右手",
                    data=data)
   
    def on_enter_selectSong(self,event):
        sender_id = event['sender']['id']
        data = [
                 {
                     "content_type": "text",
                     "title": "男歌手",
                     "payload" : "男歌手"
                 },
                 {
                     "content_type": "text",
                     "title": "女歌手",
                     "payload" : "女歌手"
                 }
             ]
        quick_reply_message(id = sender_id,text = "請選擇歌曲類型：",quick_replies=data)
    def on_enter_continueSong(self,event):
        sender_id = event['sender']['id']
        data = [
                 {
                     "content_type": "text",
                     "title": "好",
                     "payload" : "好"
                 },
                 {
                     "content_type": "text",
                     "title": "不要",
                     "payload" : "不要"
                 }
             ]
        quick_reply_message(id = sender_id,text = "要繼續遊戲嗎？",quick_replies=data)
                
    
    def on_enter_Song(self,event):
        global sex
        global songName
        sender_id = event['sender']['id']
        send_text_message(sender_id,u'請根據以下歌詞猜出完整歌名：')
        while(True):
            if(sex):
                url = "https://mojim.com/" + random.choice(boy) + ".htm"
            else:
                url = "https://mojim.com/" + random.choice(girl) + ".htm"
            page = requests.get(url).text
            singer = {}
            htm = soup(page,'html.parser')
            items = htm.select("span.hc3 > a")
            for item in items:
                if item.text != u"(提供)":
                    if item.text.find("(") == -1 and item.text.find("/") == -1:
                        name = item.text
                        link = item.get('href')
                        singer[name] = link

            prob = random.choice(list(singer.keys()))
    
#print(singer[prob])
            netlink = 'https://mojim.com' + singer[prob]
            page = requests.get(netlink).text
            htm = soup(page,'html.parser')
            items = htm.select("dd.fsZx3")
            sen = []
            prob2 = []
            signal = False
            for item in items:
                sen = str(item).split('<br/>')
            sen = sen[0:-2]
            for s in sen:
                 s = s.decode('utf-8')
                 if s.find(u'作曲') != -1:
                     signal = True
                     continue
                 if signal:
                     if s.find('[') != -1 or s.find('---') != -1:
                         break;
                     if s.find(u'更多更詳盡歌詞') == -1 and s.find(u'編曲') == -1 and s.find(u'合唱') == -1 and s.find(u'製作人') == -1 and s != '':
                         prob2.append(s)
            if(prob2 != []):
                txt = random.choice(prob2).strip()
                #print(prob)
                songName = prob
                send_text_message(sender_id,random.choice(prob2))
                break


    def on_enter_FEcolor(self,event):
        sender_id = event['sender']['id']
        data = [
                {
                    "type" : "postback",
                    "title" : u"劍 槍 斧 弓 藍弓 綠弓 暗器 赤暗器",
                    "payload": u"劍 槍 斧 弓 藍弓 綠弓 暗器 赤暗器"
                },
                
                {
                    "type" : "postback",
                    "title" : u"藍暗器 綠暗器 杖 紅法 藍法 綠法",
                    "payload": u"藍暗器 綠暗器 杖 紅法 藍法 綠法"  
                },
                {
                    "type" : "postback",
                    "title" : u"紅龍 藍龍 綠龍 無龍",
                    "payload": u"龍類"  
                }               ]
        template_message(
                   id = sender_id,
                    title="查詢聖火手遊資料",
                    img_url="https://gamewith.akamaized.net/service/hd/images/4e178425888821289c228a06eabf1a92.png",
                    subtitle="選擇英雄武器",
                    data=data)



    def on_enter_FEmove(self,event):
        global url        
        sender_id = event['sender']['id']
        

        data = [
                {
                    "type" : "postback",
                    "title" : u"步行 騎兵 重甲 飛行",
                    "payload": u"步行"
                }
             ]
        template_message(
                   id = sender_id,
                    title="查詢聖火手遊資料",
                    img_url="https://gamewith.akamaized.net/assets/images/games/covers/2014695d15dd044439789ee9023ad105.png",
                    subtitle="選擇移動方式",
                    data=data)
    def on_enter_Hero(self,event):
        global url
        global condition
        global lang
        sender_id = event['sender']['id']
        page = requests.get(url).text
        htm = soup(page,'html.parser')
        name = ''
        link = ''
        hero = False;
        signal = False
        lang = {}
        items = [elem for elem in htm.find_all('a',class_ = "a-link")]
        for item in items:
            if item.get('href')[0] == '/':
                continue
            if item.text == u'杖' and url[-6:] == '210813':
                signal = True
                continue
            if item.text == u'無竜':
                signal = True
                continue
            if(signal):
                hero = not hero
                if item.text == u'赤属性':
                    break;
        #print(item.text)
        #print(item.get('href'))
                if hero:
                    name = item.text
                    link = item.get('href')
        
                if not hero:
                    if item.text == condition:
                        lang[name] = link
                       

        if lang:
            send_text_message(sender_id,u'請輸入你想查詢的對象：')
            for Name in lang.keys():
                send_text_message(sender_id,Name)
            
        else:
            send_text_message(sender_id,u'並沒有符合你的期待的英雄')
            self.go_back()
    def on_enter_Hero2(self,event):
        
        sender_id = event['sender']['id']
        
        data = [
                {
                    "type" : "postback",
                    "title" : u"英雄標準體質",
                    "payload": u"英雄標準體質"
                },
                {  
                    "type" : "postback",
                    "title" : u"擁有技能",
                    "payload": u"擁有技能"
                }, 
                {  
                    "type" : "postback",
                    "title" : u"看照片",
                    "payload": u"看照片"
                } 
             ]
        template_message(
                   id = sender_id,
                    title=u"查詢聖火手遊資料",
                    img_url="https://gamewith.akamaized.net/assets/images/games/covers/2014695d15dd044439789ee9023ad105.png",
                  
                    subtitle=u"選擇想要的操作",
                    data=data)

    def on_enter_NOP(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'還有這種操作？')
        self.go_back()

    def on_enter_FEimage(self,event):
        global link
        sender_id = event['sender']['id']
        page = requests.get(link).text
        htm = soup(page,'html.parser')
        sign = False
        items = [elem for elem in htm.find_all('img',class_ = "a-img",alt = re.compile(u"立ち絵$"))]
        for item in items:
            send_image(sender_id,item.get('src'))    
        send_text_message(sender_id,u"是否繼續查詢？")

    def on_enter_FEskill(self,event):
        global link
        sender_id = event['sender']['id']
        
        page = requests.get(link).text
        htm = soup(page,'html.parser')
        sign = False
        skill = []
        recommend = []
        items = [elem for elem in htm.find_all('a',class_ = "a-link")]
        for item in items:
            if item.text == u"▶覚醒おすすめの星4キャラランキング":
                sign = True
                continue;
            if item.text == u"▶スキル継承素材キャラクターまとめ":
                break;
            if sign:
                txt = item.text
                if txt in skill:
                    recommend.append(txt)
                else:
                    skill.append(txt)
        send_text_message(sender_id,u'持有技能：')
        for sk in skill:
            send_text_message(sender_id,sk)
        send_text_message(sender_id,u'建議繼承技能：')
        for rc in recommend:
        
            send_text_message(sender_id,rc)
        send_text_message(sender_id,u"是否繼續查詢？")
    def on_enter_FEbody(self,event):
        global link
        sender_id = event['sender']['id']
        page = requests.get(link).text
        htm = soup(page,'html.parser')
        sign = False
        index = 1
        items = [elem for elem in htm.find_all('td',class_ = "center",string = re.compile("^()"))]
        for item in items:
            if int(item.text) > 100:
                break
            index = index + 1

        attr = items[index:index + 6]#8 14
        send_text_message(sender_id,u'lv.40空裝體質：')
        send_text_message(sender_id,u"HP:" + attr[0].text)
        send_text_message(sender_id,u"攻擊:" + attr[1].text)
        send_text_message(sender_id,u"速度:" + attr[2].text)
        send_text_message(sender_id,u"防守:" + attr[3].text)
        send_text_message(sender_id,u"魔防:" + attr[4].text)
        send_text_message(sender_id,u"是否繼續查詢？")
