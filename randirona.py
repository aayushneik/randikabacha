import colorama
import pyfiglet

colorama.init()
print(colorama.Fore.RED)
print(colorama.Style.BRIGHT)
f = pyfiglet.Figlet(font='slant')
print (f.renderText('omar'))
f = pyfiglet.Figlet(font='slant')
print (f.renderText('proxt'))
f = pyfiglet.Figlet(font='digital')
print (f.renderText('omar prox t'))

print("""
Youtube:
https://youtube.com/channel/UCFhrrvVJpnlIlXW4sB4YxnA

instagram : https://www.instagram.com/omar_proxt/

Amino :
http://aminoapps.com/p/saer6z

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

""")
dec = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━' 
import aminofix,requests
from threading import Thread as t
clint=aminofix.Client()
clint.login(email=input("email ••> : "),password=input("password ••> : "))
headers=clint.headers
x=clint.get_from_code(code=input("chat link ••> "))
com=[]
x1=clint.get_from_code(input("community link   ••> "))
comId=x.path[1:x.path.index('/')]
chatId=x.objectId
subclint=aminofix.SubClient(comId=comId,profile=clint.profile)
subclin=aminofix.SubClient(comId=x1.path[1:x1.path.index('/')],profile=clint.profile)
userI=[]
s=0
size=100
while (s!=1500):
		user=subclin.get_online_users(start=s,size=size).profile.userId
		for o in user:
			userI.append(o)
		s+=100
		size+=100
print(userI)
def send():
	for i in range(100):
			try:
				subclint.edit_chat(chatId=chatId,coHosts=userI)
			except:
				print("فـلـسـ𝐏𝐚𝐥𝐞𝐬𝐭𝐢𝐧𝐞ـطـيـن🇵🇸")
def all():
	while True:
		t(target=send).start()
all()