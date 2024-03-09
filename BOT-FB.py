#!/usr/bin/python3
#coding=utf-8

import re, bs4, requests, time, sys, os, random, json, time,datetime

logo = ('''\033[1;92m
 _______  _______         _______  _______  _______ 
|       ||  _    |       |  _    ||       ||       |
\033[1;97m|    ___|| |_|   | ____  | |_|   ||   _   ||_     _|
|   |___ |       ||____| |       ||  | |  |  |   |  
|    ___||  _   |        |  _   | |  |_|  |  |   |  
|   |    | |_|   |       | |_|   ||       |  |   |  
\033[1;92m|___|    |_______|       |_______||_______|  |___|  \033[1;97m
''')

bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = bulan[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+" "+str(bln)+" "+str(thn)

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "Selamat Dini Hari !"
elif 4 <= hour < 12:
  hhl = "Selamat Pagi !"
elif 12 <= hour < 15:
  hhl = "Selamat Siang !"
elif 15 <= hour < 17:
  hhl = "Selamat Sore !"
elif 17 <= hour < 18:
  hhl = "Selamat Petang !"
else:
  hhl = "Selamat Malam !"

def login():
        os.system('clear')
        print (logo)
        cookie = input('- cookie : ')
        try:
            cari = requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":cookie})
            token = re.search("(EAAG\w+)", cari.text).group(1)
            if "EAAG" in str(token):
                open('cookie.txt','w').write(cookie)
                open('token.txt','w').write(token)
                bot_komen()
        except AttributeError:
        	exit("- cookie sudah kedaluwarsa !!!")
        except requests.exceptions.ConnectionError:
        	exit("- koneksi internet bermasalah !!!")

def bot_komen():
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	os.system("clear")
	print (logo)
	idx = input(f"\033[1;97m- id target : ")
	cek = requests.get("https://graph.facebook.com/"+idx+"?access_token="+token,cookies=coki).json()
	lim = input(f"\033[1;97m- limit : ")
	print("")
	post = requests.get("https://graph.facebook.com/"+cek['id']+"?fields=feed.limit("+lim+")&access_token="+token,cookies=coki).json()
	for i in post['feed']['data']:
		tag = ("@["+ idx +":]");f = open("motivasi.txt","r");lines = f.readlines();f.close();texs = random.choice(lines);kom = ("Komentar Ini Ditulis Oleh Bot ");waktu = str(datetime.datetime.now().strftime('%H:%M:%S'));_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
		submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + hhl + "\n"+ tag + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
		if 'id' in submit:
			print(f"\033[1;92m[✓] SUCCES : "+submit['id'])
		else:
			print(f"\033[1;91m[!] FAILED : "+i['id'])
	
	print(f"\n\033[1;97m- finished...")
	input(f"\n\033[1;97m[<BACK>]")
	bot_komen()
	
login()