#!/bin/python
import asyncio,sys,os,names,re,csv,\
requests,\
json,random,socks,\
time,traceback
import configparser as cp
import telethon
from telethon import TelegramClient
from telethon import connection as conn
if(os.name=='posix'):
 import readline
else:
 pass
class telegram:
 def __init__(self,api_id,api_hash,proxy_choosing='Random',proxy=None,proxy_type=str(),proxy_list=str()):
  self.api_id=api_id;self.api_hash=api_hash;
  p_list=['mt_proxy','socks5']
  if proxy_type not in p_list:
   proxy_type=None
  print(proxy,proxy_type)
  if(type(proxy)==tuple and len(proxy)==3):
   self.proxy=proxy
  else:
   self.proxy=None
  self.proxy_type=proxy_type
  #print(locals())
#  print(proxy_list,os.path.isfile(proxy_list))
  if(os.path.isfile(proxy_list)==False and self.proxy_type!=None):
   proto=self.proto=parser.get(proxy_type,'protocol') if proxy_type.lower() in p_list else None
   server=self.server=parser.get(proxy_type,'host') if proxy_type.lower() in p_list else None
   port=self.port=parser.get(proxy_type,'port') if proxy_type.lower() in p_list else None
   secret=self.secret=parser.get(proxy_type,'secret') if proxy_type.lower() in p_list else None
  elif(os.path.isfile(proxy_list)==True and self.proxy_type!=None):
   lines=open(proxy_list).readlines()
   self.proxies=[str(i).strip().split(":")\
    for i in lines if not(str(i).startswith('#'))]
   p=random.choice(self.proxies)
   server=p[0]
   port=p[1]
   secret=p[2]
   try:
    proto=p[3].capitalize()
    if not(proto in conns):
     raise Exception('wrong protocol')
   except:
    proto='Randomized intermediate'
   conns={
    'Abridged':conn.ConnectionTcpMTProxyAbridged,
    'Intermediate':conn.ConnectionTcpMTProxyIntermediate,
    'Randomized intermediate':conn.ConnectionTcpMTProxyRandomizedIntermediate
    }
   self.proxy=(server,port,secret)
   self.connection=conns.get(proto)
   print(*self.proxy)
   #print(proto,self.connection)
 def create_account(self,number,fname='user'\
 ,lname=str(),accs_file='created_accounts.json',\
 code=lambda :'code'):
  print(number,fname,lname)
  self.accs_file=accs_file
  self.fname=fname
  self.lname=lname
  self.number=number
  self.session_name=f'sessions/{fname}-{lname}_{number}'
  self.code=str(code())
  #print(f"'{self.code}'")
  try:
   if(self.proxy_type!=None):
    client = TelegramClient(self.session_name,\
      self.api_id, self.api_hash,connection=self.connection,proxy=self.proxy)
   else:
    client = TelegramClient(self.session_name,\
     self.api_id, self.api_hash)
   if(re.fullmatch('[0-9]{5}',self.code)!=None):
     client.start(\
       phone=number,\
       force_sms=True,\
       first_name=fname,\
       last_name=lname,\
       code_callback=lambda :self.code)
     self.set_log('Done')
   elif(self.code=='Canceled'):
    self.clear_session()
    self.set_log('CANCELED')
    return 'Canceled'
   elif(self.code=='NO_RESPONSE'):
    self.clear_session()
    self.set_log('NO_RESPONSE')
    return 'No Response'
    #self.clear_session()
   else:
    self.set_log('CODE_ERROR')
    #print(f'"{self.code}"')
    self.clear_session()
    return 'CodeError'
  except telethon.errors.rpcerrorlist.PhoneNumberBannedError:
   self.set_log('BANNED')
   self.clear_session()
   return 'banned'
  except telethon.errors.rpcerrorlist.FloodWaitError:
   self.set_log('FLOOD')
   self.clear_session()
   return 'flood'
  except Exception as e:
   self.set_log(f"{e}{traceback.format_exc()}")
   return f"Unknown Error '{e}'"
 def set_log(self,status):
  try:
   file=open(self.accs_file)
   #print(file)
   accounts=json.load(file)
   file.close()
  except Exception as e:
   accounts=dict()
   print(e)
  self.accounts=accounts
  file=open(self.accs_file,'w')
  self.accounts.update({self.number:{
      'first name':self.fname
      ,'last_name':self.lname
      ,'time':time.ctime()
      ,'code':self.code
      ,'session':self.session_name
      ,'proxy':self.proxy
      ,'proxy_type':self.proxy_type
      ,'status':status}
     })
  #print(self.accounts)
  json.dump(self.accounts,file,indent=4)
  file.close()
 def clear_session(self,session_name=''):
  #os.chdir('sessions')
  #print('Removing',session_name)
  cwd=os.getcwd()
  if(session_name==''):
   session_name=self.session_name
  #os.remove(f"{cwd}/"+session_name+'.session')
  color(f'!session$:@{session_name} !removed')
  #os.chdir('..')
  pass
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
   #print(answer)
   try:
    self.number_id=answer['ACCESS_NUMBER'][0]
    self.number=answer['ACCESS_NUMBER'][1]
    return True
   except:
    #print('no numbers are available')
    #sys.exit()
    return answer
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
  #print(resp.text) #i put it just for debugging
  status=resp.text
#  if( len(status.split(":")) > 1 and 'STATUS_OK' in status):
#   status={
#    status[0]:status[:1]
 #  }
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
  #self.get_code_status=status
  return status
 def finish(self,n_id=''):
  if(n_id==''):
   n_id=self.number_id
  payload={
   'api_key':self.token,
   'action':'setStatus',
   'status':'9',
   'id':n_id
   }
  resp=requests.get(self.api_url,params=payload)
  status=resp.text
  #self.get_code_status=status
  return status
 def return_code(self,wait=5,times=10):
  i=1
  self.ask_for_code()
  while(True):
   status=self.get_code()
   if(status=='ACCESS_CANCEL' or status=='STATUS_CANCEL'):
    return 'Canceled'
   i=i+1
   color(f'$[!{i}$]%{self.number},!status $:@{status}! Waiting %@{wait} !seconds').print(end='\r')
   time.sleep(wait)
   if(i>=times):
    #color('%The API is not responding$............').print()
    #self.cancel()
    #sys.exit()
    return 'NO_RESPONSE'
   if(type(status)==str):
    if(status.split(":")[0]!='STATUS_WAIT_CODE'):
     if(status.split(":")[0]=='STATUS_OK'):
      code=status.split(':')[1]
      print(code)
      return code
     break
     return False
  return False
def cli():
 api_key=parser.get('sim_api','active_ru_key')
 sms=sms_api(key=api_key)
 cli.sms=sms
 balance=sms.get_balance()
# print(balance)
 #cli.proxy_type=parser.get('telegram','proxy_type')
 cli.balance=balance
 color(f'!current_balance$:%{balance} $Rub^').print()
 #if(re.fullmatch(r'(\d{1,3}\.){3}\d{1,3}:(\d+)',cli.proxy)!=None):
 # proxy_host=cli.proxy.split(':')[0]
 # proxy_port=cli.proxy.split(':')[1]
 # tg_session=telegram(parser.get('telegram','api_id'),\
 #     parser.get('telegram','api_hash'),\
 #     proxy=(socks.SOCKS5,cli.proxy[0],cli.proxy[1])\
 #     )
 #else:
 if(parser.get('telegram','proxy_from_list')=='False'):
  tg_session=telegram(parser.get('telegram','api_id'),\
        parser.get('telegram','api_hash'),\
        proxy_type=parser.get('telegram','proxy_type'),
        )
 else:
  tg_session=telegram(parser.get('telegram','api_id'),\
        parser.get('telegram','api_hash'),\
        proxy_type=parser.get('telegram','proxy_type'),\
        proxy_list=parser.get('telegram','proxy_list')
        )
  #print(parser.get('telegram','proxy_list'))
 #country=random.choice(list(sms.countries.keys()))
 #print(country)
 cli.bal=balance
 country=parser.get('sim_api','country')
 cli.land=country
 buy_status=sms.buy(country=country)
 if(buy_status!=True):
  #status=buy_status
  return list(buy_status.keys())[0]
 number=sms.number
 try:
  cli.tg_status=tg_session.create_account(number,\
  code=lambda :sms.return_code(
   wait=int(parser.get('sim_api','sms_timeout')),
   times=int(parser.get('sim_api','sms_wait_times'))
   ),\
  fname=names.get_first_name(),\
  lname=names.get_last_name())
  if(cli.tg_status!='done'):
   sms.cancel()
   #tg_session.clear_session()
   pass
 except Exception as e:
  print(e,sms.cancel(),traceback.format_exc())
  return e
 return cli.tg_status
#global truthy
def prompt(cmd=str()):
 cmd=cmd.lower()
 truthy=list()
 if(cmd in ['help','?','h']):
  color('''
   !h$|!help$|!?      $: %returning this help message
   !TGConfig      $: %to print telegram config
   !register $<!number$> $:%to register a new number
                           $(%no !API$)
   !bal$|!balance      $: %to print SMS API balance
   !APIConfig     $: %to print SMS API config
   !start $[!times$] $: %to start the script
   !examples$:
    #Making 10 accounts:
      @start 10
    #Making a single account:
      @start'''
  ).print()
  return True
 elif('set' in cmd):
  args=cmd.split('\x20')
  sim_api_items=dict(parser.items('sim_api'))
  tg_api_items=dict(parser.items('telegram'))
  #print(args[1] in sim_api_items)
  config=None
  if(len(args)>2):
   if(args[1] in sim_api_items):
    config='sim_api'
   elif(args[1] in tg_api_items):
    config='telegram'
   else:
    #print('')
    pass
   if(config!=None):
    if(args[1] in ['Mt_proxy','Socks5_proxy']):
     parser.set(config,args[1],args[2])
    else:
     parser.set(config,args[1],args[2].capitalize())
    color(f'!{args[1]} $-> @{args[2].capitalize()}').print()
    return True
   else:
    print(f'unknown option "{args[1]}" ')
    return False
  else:
   print(f'No enough arguments for command "{args[0]}"')
   return False
 elif('register' in cmd):
  args=cmd.split('\x20')
  tg_session=telegram(parser.get('telegram','api_id'),\
  parser.get('telegram','api_hash'))
  try:
   status=tg_session.create_account(args[1],code=lambda :input('[*] Code:'))
   print(status)
   return True
  except:
   print('error')
   return False
 elif(cmd in ['bal','balance']):
  api_key=parser.get('sim_api','active_ru_key')
  sms=sms_api(key=api_key)
  balance=sms.get_balance()
  color(f'available !balance $:%{balance}').print()
  return True
 elif(cmd in [str(),'\n']):
  pass
 elif(cmd.startswith('!')):
  os.system(cmd[1:])
 elif(cmd in ['tgconfig','tgconf','tgc','telegramconf']):
  tgconfig=dict(parser.items('telegram'))
  for conf,val in tgconfig.items():
   color(f"!{conf} $-> @{val}").print()
  return True
 elif(cmd in ['apiconfig','apiconf']):
  apiconfig=dict(parser.items('sim_api'))
  for conf,val in apiconfig.items():
   #print(f"{conf} -> {val}")
   color(f"!{conf} $-> @{val}").print()
  return True
 elif(cmd in ['proxyconfig','pconf','proxyconf']):
  apiconfig=dict(parser.items(parser.get('telegram','proxy_type') ))
  for conf,val in apiconfig.items():
   #print(f"{conf} -> {val}")
   color(f"!{conf} $-> @{val}").print()
  return True
 elif('start' in cmd):
  args=cmd.strip().split('\x20')
  if(len(args)>1):
   try:
    times=int(args[1])
    for i in range(times):
     register_status=cli()
     txt=str()
     if(register_status==True):
      txt=color('@Done').txt
      truthy.append(True)
     else:
      txt=color(f'$Fail !reason$: %{register_status} :(').txt
     color(f'![#{i+1}!]![@{cli.bal}$,#{cli.land}!]! {txt} at %{time.ctime()}^').print()
     if(register_status!=True):
      truthy.append(False)
   except Exception as e:
    color(f'$invalid syntax {e} {traceback.format_exc()}').print()
    return False
  else:
   x=cli()
   color(f'![#1!]![@{cli.bal}$,#{cli.land}!]! {x} at %{time.ctime()}^').print()
   #print(x)
   return x
 else:
  color(f'${cmd}!: %command not found.').print()
  return False
class color:
 def __init__(self,txt):
  if(os.name=='posix'):
   txt=txt.replace("!","\x1b[94m") # Light_blue
   txt=txt.replace("@","\x1b[92m") # Light_green
   txt=txt.replace("#","\x1b[95m") # Magenta
   txt=txt.replace("$","\x1b[91m") # Light_red
   txt=txt.replace("%","\x1b[93m") # Light_yellow
   txt=txt.replace("^","\x1b[0m")  # Block
  else:
   txt=txt.replace("!","") # Light_blue
   txt=txt.replace("@","") # Light_green
   txt=txt.replace("#","") # Magenta
   txt=txt.replace("$","") # Light_red
   txt=txt.replace("%","") # Light_yellow
   txt=txt.replace("^","")  # Block
  self.txt=txt
 def print(self,**args):
  print(self.txt,**args)
def startup():
 args=parser.get('startup','args').split(",")
 command=parser.get('startup','command')
 times=int(parser.get('startup','execute_times'))
 till_success=parser.get('startup','till_success')
 max_try=int(parser.get('startup','max_trys').strip())
 cmd=f'{command} {" ".join(args)}'
 color(f'!Executing Command $"#{cmd}$"! times$=@{times} !max_trys$=@{max_try} !till_sucess$=@{till_success}').print()
 for i in range(times):
  if(till_success=='True'):
   while(not(prompt(cmd=cmd))):
    print(f'retrying {i+1} times max:{max_try}')
    if(i==max_try):
     print('done')
     break
  else:
   prompt(cmd=cmd)
   print(f'trying {i+1} times max:{times}')
   pass
if __name__=='__main__':
 parser=cp.ConfigParser()
 p={
 'Mt_proxy':"!MT",
 'SOCKS5_Proxy':"$S5"
 }
 cfg=parser.read('config.ini')
 os.system('clear')
 color('^type $"!help$"^ if you need help %:$)').print()
 color('''
!╔╦╗!╔═╗   @╔═╗#┌─┐┌─┐┌─┐┬ ┬┌┐┌┌┬┐  @╔═╗#┬─┐┌─┐┌─┐┌┬┐┌─┐┬─┐
! ║ !║ ╦───@╠═╣#│  │  │ ││ ││││ │   @║  #├┬┘├┤ ├─┤ │ │ │├┬┘
! ╩ !╚═╝   @╩ ╩#└─┘└─┘└─┘└─┘┘└┘ ┴   @╚═╝#┴└─└─┘┴ ┴ ┴ └─┘┴└─
            @github.com#/%ahmed$M%ahmed$8a^ '''
            ).print()
 try:
  startup()
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
 except EOFError:
  print('GoodBye :(')
  sys.exit(0)
 except Exception as e:
  print('Error',e)
  sys.exit(1)
 while True:
  try:
   prompt(\
    cmd=input(\
    color(f'@[{p[parser.get("telegram","proxy_type")]}@]#cmd !~$>@ ').txt #coloring prompt
    ) #closing input
    )
  except KeyboardInterrupt:
   try:
    cli.sms.cancel()
    exit_prompt=str(input('\nis it time to say goodbye [Y/n]: '))
   except:
    exit_prompt='n'
   if(exit_prompt.lower()=='n'):
    print('it\'s nice being with you :)')
   else:
    print('Bye :"(')
    sys.exit(0)
  except EOFError:
   print('GoodBye :(')
   sys.exit(0)

