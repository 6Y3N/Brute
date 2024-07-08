#!/usr/bin/python3
#"""--------------------------------------------
#__ᴅᴇᴠᴇʟᴏᴘᴇᴅ__ = ___ᴅᴇᴠɪʟ ᴍᴀʏ ᴄʀʏ___'
#__ғᴀᴄᴇʙᴏᴏᴋ__ = ___ʜᴜssᴇɪɴ ᴋɪᴊᴀɴᴀ'
#__ᴛᴇᴀᴍ__ = ___ᴅᴍᴄ___'
#__ɢɪᴛ_____= ___404_ɴᴏᴛ_ғᴏᴜɴᴅ___'
#___ᴠ___= 3.4
#--------------------------------------------"""
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ᴄᴏʟᴏʀ's___'
#--------------------------------------------"""
Z = "\x1b[0;90m" # Black 
M = "\x1b[38;5;196m" # Red 
H = "\x1b[38;5;46m" # Green 
K = "\x1b[38;5;226m" # Yellow 
B = "\x1b[38;5;44m" # Blue 
U = "\x1b[0;95m" # Purple 
O = "\x1b[0;96m" # Light Blue 
P = "\x1b[38;5;231m" # White 
J = "\x1b[38;5;208m" # Orange 
A = "\x1b[38;5;248m" # Grey 
N = '\x1b[0m' # OFF COLOR 
PT = '\x1b[1;97m' # THICK WHITE 
MT = '\x1b[1;91m' # BOLD RED 
HT = '\x1b[1;92m' # BOLD GREEN 
KT = '\x1b[1;93m' # BOLD YELLOW 
BT = '\x1b[1;94m' # BOLD BLUE 
UT = '\x1b[1;95m' # THICK PURPLE 
OT = '\x1b[1;96m' # BOLD LIGHT 
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ᴄᴏʟᴏʀ2___'
#--------------------------------------------"""
Z2 = "[#000000]" # BLACK 
M2 = "[#FF0000]" # RED 
H2 = "[#00FF00]" # GREEN 
K2 = "[#FFFF00]" # YELLOW 
B2 = "[#00C8FF]" # BLUE 
U2 = "[#AF00FF]" # PURPLE 
N2 = "[#FF00FF]" # PINK 
O2 = "[#00FFFF]" # LIGHT BLUE 
P2 = "[#FFFFFF]" # WHITE 
J2 = "[#FF8F00]" # ORANGE 
A2 = "[#AAAAAA]" # GRAY
DMC = '{ DMC }'
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ᴍᴏᴅᴜʟᴇs___'
#--------------------------------------------"""
import os,re,random,uuid,subprocess,requests,sys,gtts
from os import system
import time, json, string,rich 
from rich.console import Console as dc
from rich.panel import Panel as dp
from rich.markdown import Markdown as dm
from rich import print
from rich.progress import track as dt
os.system("pkg install play-audio")
os.system("pkg install gtts")
os.system('rm -rf .a.txt')
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ɪɴsᴛᴀʟʟ___'
#--------------------------------------------"""
try:
	import mechanize
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
except:
	os.system('pip install mechanize')
 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def back():
    main_menu()
def linex():
	print('----------------------------------------------')
def contact():
	os.system('xdg-open https://wa.me/+2348119592170 ')
	back()
G = "\u001b[32m"
B = "\u001b[36m"
W = "\033[1;37m"
pemisah = '|'
q="968"
qq="8280"
qqq="52729"
qqqq="420"
client_id = f"{qqqq}038{q}89{qq}485649{qqq}208"
sim_hini = str(random.randint(2e4,4e4))
trace_id = str(uuid.uuid4())
 
try:
	android = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '').upper()
	model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '').upper()
	carrier = '' + subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '').upper()
except:
	android = random.choice(['TECNO', "INFINIX", "SAMSUNG"])
	model = random.choice(['LD2', "SM-J009", "SM-J505", "HOT12", "NOTE-11", "A5-PRO"])
	carrier = '' + random.choice(['02', 'Oramge', 'EE', "At&", "MTN", "Cricket"])
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ʀᴏʙᴏᴛ___'
#--------------------------------------------"""
"""
pkg install play-audio
pip install gtts
"""
import os
try:
    import gtts
except:
    
    os.system("pip install gtts")
from gtts import gTTS

def create_(text,file):
    my_a = gTTS(text)
    my_a.save(file)


def play_audio(audio_file):
    os.system("play-audio "+audio_file)
    

def dual(text,file):
    create_(text,file)
    play_audio(file)

dual("welcome to bitch","l.mp3")
os.system('clear')
def looood(dmxx):
    for i in dt(range(500),description=dmxx):
        time.sleep(0.01) 



looood("OWI API TZY")
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ᴄʟᴇᴀʀ___'
#--------------------------------------------"""
def dclr():
	os.system("cls" if os.name == "nt" else "clear")
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ʟᴏɢᴏ___'
#--------------------------------------------"""
def dmc():
    dclr()
    dc(width=50, style="bold green").print(
        dp(
            """[bold green] [bold white] [bold green]
[bold green] SESCE DUMP UNLIMITED 
[bold green] VERSION 1.8
[bold white] [bold blue]""",
            title="[bold green]●[bold white]●[bold green]●[bold green] HELO [bold white] GUA [bold green] Y3N_STS [bold green]●[bold white]●[bold green]●",
        )
    )
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ʟᴏɢɪɴ___'
#--------------------------------------------"""
class login():
	def __init__(self):
		ids=[]
	def lo_epa(self):
		system('clear')
		dmc()
		em = input(f'ID FB/EMAIL: ')
		ps = input(f'MASUKAN SANDI: ')
		e="5990"
		ee="655"
		eee="59"
		tok1 = f"2377{e}9{eee}1{ee}"
		ei="0f140aabedfb65"
		ei2="a2263b1"
		tok2 = f"25257C{ei}ac27a739ed1{ei2}"
		us = f'Mozilla/5.0 (Linux; Android {str(random.randint(4,11))}.0; Nexus 5 Build/MRA{str(random.randint(30,60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600,1661))}.41'
		br.addheaders = [('User-Agent', us)]
		li = "b-ap"
		lo = "od/auth.l"
		op="3f555f98"
		op2 = "d7aa0c"
		op3="58f522efm"
		sig=f"{op}fb61fc{op2}44f{op3}"
		p = br.open(
			'https://'+li+'i.facebook.com/meth'+lo+'ogin?access_token='+tok1+'%'+tok2+'&format=json&sdk_version=1&email=' + em + '&locale=en_US&password=' + ps + '&sdk=ios&generate_session_cookies=1&sig='+sig+'')
		po = json.load(p)
		if 'access_token' in po:
			toke=po['access_token']
			linex()
			animation(f'LOGIN BERHASIL')
			open('.token.txt','w').write(toke)
			exit()
		else:
			if 'www.facebook.com' in po['error_msg']:
				dc(width=50, style="bold green").print(
            dp(
                "[italic green]ᴀᴄᴄᴏᴜɴᴛ  [bold white] ɪs ɪɴ[bold green] ᴄʜᴇᴄᴋᴘᴏɪɴᴛ[bold green] ᴜsᴇ ᴀɴᴏᴛʜᴇʀ ᴀᴄᴄᴏᴜɴᴛ [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
				exit(em+'|'+ps)
			else:
				linex()
				exit(f'{M2} ᴡʀᴏɴɢ ɪᴅ/ᴇᴍᴀɪʟ ᴏʀ ᴘᴀssᴡᴏʀᴅ\033[0m')
	def login_epa2(self):
		system('clear');
		dmc()
		cooke = input(f'{P2}◄●►{H2}ᴄᴏᴏᴋɪᴇ : ')
		cookie = {'Cookie': cooke}
		xyz = requests.session()
		data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
		req = xyz.post('https://graph.facebook.com/v16.0/device/login/', data=data).json()
		cd = req['code']
		ucd = req['user_code']
		url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038' % (
			cd)
		req = bs(xyz.get('https://mbasic.facebook.com/device', cookies=cookie).content, 'html.parser')
		raq = req.find('form', {'method': 'post'})
		dat = {'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
			   'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(req)).group(1), 'qr': '0',
			   'user_code': ucd}
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
		dat = {}
		raq = pos.find('form', {'method': 'post'})
		for x in raq('input', {'value': True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']: x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
		req = xyz.get(url, cookies=cookie).json()
		if 'access_token' in req:
			dc(width=50, style="bold green").print(
            dp(
                "[italic green] LOGIN  [bold white] SUCESFULL [bold green] JALANKAN ULANG [bold green] [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
			open('.token.txt', 'w').write(req['access_token'])
			exit()
		else:
			exit(f'{M2} ɪɴᴠᴀʟɪᴅ ᴄᴏᴏᴋɪᴇ ᴏʀ sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ')
	def login_WALA(self):
		system('clear');dmc()
		dc(width=50, style="bold green").print(
        dp(
            "[italic green]1.[italic white] ʟᴏɢɪɴ ᴡɪᴛʜ ɪᴅ ᴘᴀss  [bold white][[bold green]ᴏɴ[bold white]] \n[italic green]2.[italic white] ʟᴏɢɪɴ ᴡɪᴛʜ ᴄᴏᴏᴋɪᴇs  [bold white][[bold read]ᴏғғ[bold white]]\n[italic green]3.[italic white] ᴇɴᴛᴇʀ ᴛᴏ ʙᴀᴄᴋ",
            subtitle="╭───",
            subtitle_align="left",
            title="[bold green]●[bold white]●[bold green]●[bold green] ʟᴏɢɪɴ [bold white]◄●► [bold green]ᴍᴇɴᴜ [bold green]●[bold white]●[bold green]●",
        )
    )
		menu = dc().input("[bold green]   ╰─> ")
		if menu in ['01', '1', 'A', 'a']:
			login().lo_epa()
		if menu in ['02', '2', 'B', 'b']:
			login().login_epa2()
		if menu in ['00', '0', 'C', 'c']:
			back()
		else:
			linex()
			animation(' [×] sᴇʟᴇᴄᴛ ᴄᴏʀʀᴇᴄᴛʟʏ ')
			time.sleep(1)
			login_WALA()
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ᴍᴇɴᴜ___'
#--------------------------------------------"""
def main_menu():
	os.system("clear");dmc()
	dc(width=50, style="bold green").print(
        dp(
            "[italic green]1.[italic white] SIMPEL  [bold white]  [[bold green]ON[bold white]] \n[italic green]2.[italic white] UNLIMITED [bold white][[bold green]ON[bold white]]",         
            subtitle="╭───",
            subtitle_align="left",
            title="[bold green]●[bold white]●[bold green]●[bold green] MENU [bold green]●[bold white]●[bold green]●",
        )
    )
	xo = dc().input("[bold green]   ╰─> ")
	if xo in ['01','1', 'A', 'a']:
		file_create_menu().file_simple()
	if xo in ['02','2', 'B', 'b']:
		file_create_menu().file_unlimmited()
	if xo in ['03','3', 'c', 'C']:
		remove_dub()
	if xo in ['04','4', 'D', 'd']:
		contact()
	if xo in ['00','0', 'E', 'e']:
		os.system('rm -rf .token.txt')
		linex()
		animation(f" [√] ᴅᴏɴᴇ ʟᴏɢᴏᴜᴛ + ᴅᴇʟᴇᴛᴇ ᴄᴏᴏᴋɪᴇ ")
		exit()
	else:
		linex()
		animation(' [×] sᴇʟᴇᴄᴛ ᴄᴏʀʀᴇᴄᴛʟʏ ')
		time.sleep(1)
		main_menu()
siid=[]
sep=[]
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ғɪʟᴇ_ᴄʀᴇᴀᴛᴇ___'
#--------------------------------------------"""
class file_create_menu():
	def file_simple(self):
		os.system('clear');dmc()
		try:
			dc(width=50, style="bold green").print(
            dp(
                "[italic green]ᴡʀɪᴛᴇ  [bold white]ғɪʟᴇ[bold green]sdcard[bold white]ɴᴀᴍᴇ[bold green]ᴡʜɪᴛʜᴏᴜᴛ /sᴅᴄᴀʀᴅ [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
			nm  = input(f'{P2} {H2} MASUKAN FILE ANDA : ').replace(' ','_')
			lk = '/sdcard/'
			lok = '%s%s'%(lk,nm)
			open(lok,'w')
		except FileNotFoundError:
			dc(width=50, style="bold green").print(
            dp(
                "[italic green] ʟᴏᴄᴀᴛɪᴏɴ ɴᴏᴛ [bold white]/[bold green]ғᴏᴜɴᴅ[bold white]/[bold green]ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
			time.sleep(2)
			back()
		except IsADirectoryError:
			time.sleep(1)
			file_create_menu().file_simple()
		if IOError:
			pass
			print(f'{P2}◄●►{H2} ᴘᴀsᴛᴇ ᴜɪᴅ ᴏɴᴇ ʙʏ ᴏɴᴇ ')
			linex()
			while True:
				ids_all = input(f"{P2}◄●►{H2} ᴇɴᴛᴇʀ ᴜɪᴅ : ")
				if ids_all == "":
					linex()
					print(f'{P2}◄●►{H2}ғɪʟᴇ sᴀᴠᴇ ᴀs : {lok} ')
					input(f'{P2}◄●►{H2} ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ʙᴀᴄᴋ ')
					back()
					break
				try:
					uid = ids_all.split("|")[0]
				except:
					uid = ids_all
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth "+self.token+"",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f' {M2} sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ᴡɪᴛʜ {uid}\033[0m ')
					if len(data) < 100:
						print(f' {P2}{H2} CP {uid} ')
						linex()
					else:
						for edge in data:
							node = edge['node']
							open(lok, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
						try:
							total_idss=len(open(lok,'r').readlines())
						except:
							total_idss='-'
						print(f'{P2}{H2} [OK] {uid} [{total_idss}] \033[0m')
						linex()
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f" [×] ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴇʀʀᴏʀ - ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ")
	def __init__(self):
		try:
			os.system('.a.txt')
			os.system('.temp.txt')
			os.remove('.temp.txt')
			os.remove('.a.txt')
		except:
			pass
		self.ids = []
		self.total = []
		self.loop = 0
		try:
			self.token = open('.token.txt', 'r').read()
			uid="100061689760374"
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth "+self.token+"",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				if not posted['data']['user']['friends']['edges']:
				    os.system('clear');dmc()
				    os.system('.token.txt')
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' {M2} sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ᴡɪᴛʜ ᴛʜɪs ɪᴅ \033[0m ')
					os.system('.token.txt')
					exit()
			except Exception as e:
				os.system('clear');dmc()
				print(f" [{M2}◄●►{P2}] ᴄᴏᴏᴋɪᴇs ᴇxᴘɪʀᴇᴅ !")
				print(e)
				login.login_WALA('')
		except Exception as e:
			print(e)
			login.login_WALA('')
	def file_unlimmited(self):
		os.system('clear');dmc()
		dc(width=50, style="bold green").print(
            dp(
                "[italic green]MASUKAN[bold white][bold green][bold green] ID YANG BERSIFAT PUBLIK[italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
		limit = input(f" MAU BERAPA ID : ")
		try:
			dc(width=50, style="bold green").print(
            dp(
                "[italic green]CONTOH[bold white][bold green][bold green] KAMBING.txt[italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
			nm  = input(f'CONTOH MACAM DI ATAS: ').replace(' ','_')
			lk = '/sdcard/'
			lok = '%s%s'%(lk,nm)
			open(lok,'w')
		except FileNotFoundError:
			dc(width=50, style="bold green").print(
            dp(
                "[italic green] ʟᴏᴄᴀᴛɪᴏɴ ɴᴏᴛ [bold white]/[bold green]ғᴏᴜɴᴅ[bold white]/[bold green]ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
			time.sleep(2)
			back()
		except IsADirectoryError:
			time.sleep(1)
			file_create_menu().file_simple()
		if IOError:
			pass
			os.system('clear');dmc()
			try:
				file = open('.temp.txt', 'r').read().splitlines()
			except:
				file = []
			os.system('clear');dmc()
			for i in range(int(limit)):
				uid = input("MASUKAN ID YANG KE {} : ".format(i+1))
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth " + self.token + "",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":4050}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f' {M2} sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ᴡɪᴛʜ {uid}\033[0m ')
					if len(data) < 100:
						print(f' [{M2}[{P2}] CP {uid} ')
					else:
						for edge in data:
							node = edge['node']
							open('.a.txt', 'a', encoding='utf-8').write(node['id'] + '\n')
							idss = len(open('.a.txt','r').readlines())
						print(f' {P2}{H2} [0K] <=> {uid} [{idss}]\033[0m')
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f" [{M2}×{P2}] ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴇʀʀᴏʀ - ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ")
			try:
				file = open('.a.txt', 'r').read().splitlines()
			except:
				file = [] 
			os.system('clear');dmc()
			print(f' {P2} {H2} TOTAL ID YANG TERKUMPUL: ' + str(len(file)))
			print(f' {P2} {H2} FILE AKAN DI SAVE DI: {lok} ')
			dc(width=50, style="bold green").print(
            dp(
                "[italic green]KETIK[bold white] [bold green] [bold green] CTR+Z UNTUK BERHENTI [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
			linex()
			for uid in file:
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth " + self.token + "",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f' {M2} sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ᴡɪᴛʜ {uid}\033[0m ')
					if len(data) < 100:
						print(f'{M2} {P2} DUMP CHECK {uid} ')
					else:
						for edge in data:
							node = edge['node']
							open(lok, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
						if 'y' in sep:
							perfector(lok)
						try:
							total_idss=len(open(lok,'r').readlines())
						except:
							total_idss='-'
						print(f'{P2} {H2} DUMP SUCSESFULL {uid} [{total_idss}] ')
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f"ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴇʀʀᴏʀ - ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ")
			print('ɪᴅs sᴀᴠᴇ ɪɴ {} path'.format(lok))
			print('ᴛᴏᴛᴀʟ ɪᴅs sᴀᴠᴇ ɪɴ ғɪʟᴇ {} '.format(len(open(lok,'r').read().splitlines())))
			input(' ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ʙᴀᴄᴋ ')
			exit()
 
def remove_dub():
    clear()
    dmc()
    dc(width=50, style="bold green").print(
            dp(
                "[italic green]ғɪʟᴇ ʟᴏᴄᴀᴛɪᴏɴ ᴇxᴀᴍᴘʟᴇ [bold white]/[bold green]sdcard[bold white]/[bold green]file.txt [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
    try:
        filename = dc().input("[bold green]   ╰─> ")
        sd = '/sdcard/'
        file_path = os.path.join(sd, filename)
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        lines = sorted(set(lines))
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        linex()
        dc(width=50, style="bold green").print(
            dp(
                f"{HT}sᴜᴄᴄᴇssғᴜʟʟʏ  {UT}={HT} ʀᴇᴍᴏᴠᴇᴅ [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
        print(f' {P2}◄●►{H2} sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ')
        input(f' {P2}◄●►{H2} ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ʙᴀᴄᴋ ')
        back()
    except FileNotFoundError:
        linex()
        dc(width=50, style="bold green").print(
            dp(
                "[italic green]ғɪʟᴇ ʟᴏᴄᴀᴛɪᴏɴ ɴᴏᴛ [bold white]/[bold green]ғᴏᴜɴᴅ[bold white]/[bold green]ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
        time.sleep(2)
        remove_dub()
#"""--------------------------------------------
#__ᴅᴍᴄ__ = ___ᴇɴᴅ___'
#--------------------------------------------"""
main_menu()
os.system('rm -rf .a.txt')
