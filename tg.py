#!/bin/python
import asyncio,sys,os,\
requests,readline,\
json,random,\
time,traceback
import configparser as cp
import telethon
from telethon import TelegramClient
class telegram:
 def __init__(self,api_id,api_hash):
  self.api_id=api_id;self.api_hash=api_hash
 def create_account(self,number,fname='user'\
 ,lname=str(),\
 code=lambda :'code'):
  #print(number)
  try:
    client = TelegramClient(f'sessions/{fname}_{number}',\
     self.api_id, self.api_hash)
    client.start(\
       phone=number,\
       force_sms=True,\
       first_name='user',\
       last_name='',\
       code_callback=code)
    return 'done'
  except telethon.errors.rpcerrorlist.PhoneNumberBannedError:
   return 'banned'
  except telethon.errors.rpcerrorlist.FloodWaitError:
   return 'flood'
  except Exception as e:
   return f"Unknown Error '{e}'"
class sms_api:
 def __init__(self,\
 api_url='https://sms-activate.ru/stubs/handler_api.php',\
 key=str(),product='tg'):
  self.token=key
  self.api_url=api_url
  self.product=product
  self.countries={
    "Russia": "0",
    "Ukraine": "1",
    "Kazakhstan": "2",
    "China": "3",
    "Philippines": "4",
    "Myanmar": "5",
    "Indonesia": "6",
    "Malaysia": "7",
    "Vietnam": "10",
    "Kyrgyzstan": "11",
    "Usa": "12 ",
    "Israel": "13",
    "HongKong": "14",
    "Poland": "15",
    "England": "16",
    "DCongo": "18",
    "Nigeria": "19",
    "Macao": "20",
    "Egypt": "21",
    "India": "22",
    "Ireland": "23",
    "Cambodia": "24",
    "Laos": "25",
    "Haiti": "26",
    "Ivory": "27",
    "Gambia": "28",
    "Serbia": "29",
    "Yemen": "30",
    "Southafrica": "31",
    "Romania": "32",
    "Colombia": "33",
    "Estonia": "34",
    "Canada": "36",
    "Morocco": "37",
    "Ghana": "38",
    "Argentina": "39",
    "Uzbekistan": "40",
    "Cameroon": "41",
    "Chad": "42",
    "Germany": "43",
    "Lithuania": "44",
    "Croatia": "45",
    "Sweden": "46",
    "Iraq": "47",
    "Netherlands": "48",
    "Latvia": "49",
    "Austria": "50",
    "Belarus": "51",
    "Thailand": "52",
    "Saudiarabia": "53",
    "Mexico": "54",
    "Taiwan": "55",
    "Spain": "56",
    "Algeria": "58",
    "Slovenia": "59",
    "Bangladesh": "60",
    "Senegal": "61",
    "Turkey": "62",
    "Czech": "63",
    "Srilanka": "64",
    "Peru": "65",
    "Pakistan": "66",
    "Newzealand": "67",
    "Guinea": "68",
    "Mali": "69",
    "Venezuela": "70",
    "Ethiopia": "71",
    "Mongolia": "72",
    "Brazil": "73",
    "Afghanistan": "74",
    "Uganda": "75",
    "Angola": "76",
    "Cyprus": "77",
    "France": "78",
    "Papua": "79",
    "Mozambique": "80",
    "Nepal": "81",
    "Belgium": "82",
    "Bulgaria": "83",
    "Hungary": "84",
    "Moldova": "85",
    "Italy": "86",
    "Paraguay": "87",
    "Honduras": "88",
    "Tunisia": "89",
    "Nicaragua": "90",
    "Timorleste": "91",
    "Bolivia": "92",
    "Costarica": "93",
    "Guatemala": "94",
    "Uae": "95",
    "Zimbabwe": "96",
    "Puertorico": "97",
    "Togo": "99",
    "Kuwait": "100",
    "Salvador": "101",
    "Libyan": "102",
    "Jamaica": "103",
    "Trinidad": "104",
    "Ecuador": "105",
    "Swaziland": "106",
    "Oman": "107",
    "Bosnia": "108",
    "Dominican": "109",
    "Qatar": "111",
    "Panama": "112",
    "Mauritania": "114",
    "Sierraleone": "115",
    "Jordan": "116",
    "Portugal": "117",
    "Barbados": "118",
    "Burundi": "119",
    "Benin": "120",
    "Brunei": "121",
    "Bahamas": "122",
    "Botswana": "123",
    "Belize": "124",
    "Caf": "125",
    "Dominica": "126",
    "Grenada": "127",
    "Georgia": "128",
    "Greece": "129",
    "Guineabissau": "130",
    "Guyana": "131",
    "Iceland": "132",
    "Comoros": "133",
    "Saintkitts": "134",
    "Liberia": "135",
    "Lesotho": "136",
    "Malawi": "137",
    "Namibia": "138",
    "Niger": "139",
    "Rwanda": "140",
    "Slovakia": "141",
    "Suriname": "142",
    "Tajikistan": "143",
    "Monaco": "144",
    "Bahrain": "145",
    "Reunion": "146",
    "Zambia": "147",
    "Armenia": "148",
    "Somalia": "149",
    "Congo": "150",
    "Chile": "151",
    "Furkinafaso": "152",
    "Lebanon": "153",
    "Gabon": "154",
    "Albania": "155",
    "Uruguay": "156",
    "Mauritius": "157",
    "Bhutan": "158",
    "Maldives": "159",
    "Guadeloupe": "160",
    "Turkmenistan": "161",
    "Frenchguiana": "162",
    "Finland": "163",
    "Saintlucia": "164",
    "Luxembourg": "165",
    "Saintvincentgrenadines": "166",
    "Equatorialguinea": "167",
    "Djibouti": "168",
    "Antiguabarbuda": "169",
    "Caymanislands": "170",
    "Montenegro": "171",
    "Denmark": "172",
    "Switzerland": "173",
    "Norway": "174",
    "Australia": "175",
    "Eritrea": "176",
    "Southsudan": "177",
    "Saotomeandprincipe": "178",
    "Aruba": "179",
    "Montserrat": "180",
    "Anguilla": "181",
    "Japan": "182",
    "Northmacedonia": "183",
    "Seychelles": "184",
    "Newcaledonia": "185",
    "Capeverde": "186",
    "Southkorea": "190"
}
 def get_balance(self):
  payload={
   'api_key':self.token,
   'action':'getBalance'
  }
  resp=requests.get(self.api_url,params=payload)
  if resp.status_code==200:
   bal=resp.text.split(':')
   self.balance={bal[0]:bal[1]}
  else:
   raise Exception(f'Error {resp.status_code}')
  return self.balance['ACCESS_BALANCE']
 def buy(self,operator='any',country='Vietnam',service='tg'):
  payload={
   'api_key':self.token,
   'action':'getNumber',
   'service':service,
   'operator':operator,
   'country':self.countries[country],
  }
  resp=requests.get(self.api_url,params=payload)
  if resp.status_code==200:
   answer={
    resp.text.split(':')[0]:resp.text.split(':')[1:]
   }
   try:
    self.number_id=answer['ACCESS_NUMBER'][0]
    self.number=answer['ACCESS_NUMBER'][1]
   except:
    print('no numbers are available')
    #sys.exit()
    return False
  else:
   raise Exception(f'Failed Getting the number {resp.status_code}')
  return answer
 def ask_for_code(self,n_id=''):
  if(n_id==''):
   n_id=self.number_id
   payload={
   'api_key':self.token,
   'action':'setStatus',
   'status':'1',
   'id':n_id
  }
  resp=requests.get(self.api_url,params=payload)
  if resp.status_code==200:
   status=True
  else:
   raise Exception(f'{resp.status_code}')
  return status
 def get_code(self,n_id=''):
  if(n_id==''):
   n_id=self.number_id
  payload={
   'api_key':self.token,
   'action':'getStatus',
   'id':n_id
   }
  resp=requests.get(self.api_url,params=payload)
  status=resp.text.split(':')
  status={
   status[0]:status[:1]
  }
  self.code_status=status
  #print(status)
  return status
 def cancel(self,n_id=''):
  if(n_id==''):
   n_id=self.number_id
  payload={
   'api_key':self.token,
   'action':'setStatus',
   'status':'-1',
   'id':n_id
   }
  resp=requests.get(self.api_url,params=payload)
  status=resp.text
  return status
 def return_code(self,wait=5,times=10):
  i=1
  while(self.get_code().get('STATUS_OK')!=['STATUS_OK']):
   print(f'[{i}]{self.number} {self.get_code()} {wait} seconds')
   time.sleep(wait)
   i=i+1
   if(i>=10):
    print('The server is not responding')
    self.cancel()
    sys.exit()
  code=self.code_status['STATUS_OK']
  return code
def cli():
 api_key=parser.get('sim_api','active_ru_key')
 sms=sms_api(key=api_key)
 balance=sms.get_balance()
# print(balance)
 cli.balance=balance
 tg_session=telegram(parser.get('telegram','api_id'),parser.get('telegram','api_hash'))
 #country=random.choice(list(sms.countries.keys()))
 country=parser.get('sim_api','country')
 #print(country)
 cli.bal=balance
 cli.land=country
 buy_status=sms.buy(country=country)
 if(buy_status==False):
  return False
 number=sms.number
 try:
  cli.tg_status=tg_session.create_account(number,code=sms.return_code)
 except Exception as e:
  print(e,sms.cancel(),traceback.format_exc())
def prompt(cmd=str()):
 cmd=cmd.lower()
 if(cmd in ['help','?','h']):
  print('''
   h|help|?      : returning this help message
   TGConfig      : to print telegram config
   register <number> : to register a new number without an API
   bal|balance      : to print SMS API balance
   APIConfig     : to print SMS API config
   start [times] : to start the script
   examples:
   Making 10 accounts:
     start 10
   Making a single account:
     start
  ''')
 elif(cmd=='register'):
  cmd=cmd.split('\x20')
  
 elif(cmd in ['bal','balance']):
  api_key=parser.get('sim_api','active_ru_key')
  sms=sms_api(key=api_key)
  balance=sms.get_balance()
  print(f'available balance :{balance}')
 elif(cmd in [str(),'\n']):
  pass
 elif(cmd.startswith('!')):
  os.system(cmd[1:])
 elif(cmd in ['tgconfig','tgconf','tgc','telegramconf']):
  tgconfig=dict(parser.items('telegram'))
  for conf,val in tgconfig.items():
   print(f"{conf} -> {val}")
 elif(cmd in ['apiconfig','apiconf']):
  tgconfig=dict(parser.items('sim_api'))
  for conf,val in tgconfig.items():
   print(f"{conf} -> {val}")
 elif('start' in cmd):
  args=cmd.split('\x20')
  if(len(args)>1):
   try:
    times=int(args[1])
    for i in range(times):
     register_status=cli()
     txt=str()
     if(register_status==True):
      txt='Done'
     else:
      txt='Fail :('
     print(f'[{i+1}][{cli.bal},{cli.land}] {txt} at {time.ctime()}')
   except Exception as e:
    print(f'{e} invalid syntax')
  else:
   print(cli())
 else:
  print(f'{cmd}: command not found')
  return 0
if __name__=='__main__':
 parser=cp.ConfigParser()
 cfg=parser.read('config.ini')
 print('type "help" if you need help :)')
 while True:
  try:
   prompt(cmd=input('cmd ~> '))
  except KeyboardInterrupt:
   try:
    exit_prompt=str(input('\nis it time to say goodbye [Y/n]: '))
   except:
    exit_prompt='n'
   if(exit_prompt.lower()=='n'):
    print('it\'s nice being with you :)')
   else:
    print('Bye :"(')
    sys.exit(0)
