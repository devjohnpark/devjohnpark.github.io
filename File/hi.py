import telepot
import requests
from bs4 import BeautifulSoup

def WorldCup(nat):
  url = "https://www.viagogo.com/kr/Sports-Tickets/Soccer/World-Cup-Tickets?AffiliateID=49&adposition=&PCID=PSKRGOOFOOTB9A1E2CB2C9386&AdID=603897122321&MetroRegionID=&psc=%2c&ps=%2c&ps_p=0&ps_c=16568379592&ps_ag=134116988066&ps_tg=kwd-324536089829&ps_ad=603897122321&ps_adp=%2c&ps_fi=%2c&ps_li=%2c&ps_lp=1009871&ps_n=g&ps_d=c&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkp45mTtAUEoN1sDIVApy9N0WjKRTEkOtWUuO0kZzso-_V_2QsDGNkMaAtqsEALw_wcB"
  html = requests.get(url)
  soup = BeautifulSoup(html.text, 'html.parser')
  nation = nat
  boxer = (soup.select('div.el-row-div'))
  teamfir = []
  teamsec = []
  for box in boxer:
    k = box.select_one('span.camo')
    s = box.select_one('div.t')
    w = box.select_one('div.t-b')
    
    btn = box.select_one('div.pri')
    k.select_one('strong')
    k = k.get_text()
    k = k[:k.find('-')].strip()
    teamlist = k.split('vs')
    if('vs' not in k):
      return "No SEARCH"
    teamfir = teamlist[0]
    teamsec = teamlist[1]
    #print(len(teamlist))
    #print(teamlist)
    if teamlist[0].strip() == nation:
      date = s.select_one('span.h')
      time = s.select_one('span.vmid')
      date = date.get_text()
      time = time.get_text()
      teamfir = teamlist[0]
      teamsec = teamlist[1]
      if(btn==None):
        print("NO TICKET\n")
      return "{} \n{}\n {} vs {} ".format(date , time , teamfir,teamsec)
      
    elif teamlist[1].strip() == nation:
      date = s.select_one('span.h')
      time = s.select_one('span.vmid')
      date = date.get_text()
      time = time.get_text()
      teamfir = teamlist[0]
      teamsec = teamlist[1]
      if(btn==None):
        print("NO TICKET\n")
      return "{} \n{}\n {} vs {} ".format(date , time , teamfir,teamsec)
  return "No SEARCH"

TELEGRAM_TOKEN = "5613859613:AAFoMUPlTxLRFEu6ETZRYT1EAYjbmqrmbB4"
def handler(msg):
    content_type, chat_Type, chat_id, msg_date, msg_id = telepot.glance(msg,long = True)

    if content_type == "text":
        bot.sendMessage(chat_id,"[Info]\n{}".format(WorldCup(msg["text"])))

bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler , run_forever=True)