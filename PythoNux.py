# coding=utf-8

import os
import socket
import sys
import time

Menu = raw_input('''
 ____        _   _           _   _            
|  _ \ _   _| |_| |__   ___ | \ | |_   ___  __
| |_) | |_| | __| '_ \ / _ \|  \| | | | \ \/ /
|  __/|___  | |_| | | | (_) | |\  | |_| |>  < 
|_|       |_|\__|_| |_|\___/|_| \_|\__,_/_/\_\
\n		
Powered by Adriel Freud, 0nir0n4ut - DebutySec.

	 [1] Menu
	 [2] Creditos

	[+] Escolha algumas da Opcoes acima.
	  
Interact>>> ''')

if Menu	== '1':
	fer = raw_input('''\n
######################
##                  ##
##   Ferramentas!   ##
##                  ##
######################

	[1] Scan De Portas!
	[2]
	[3]
	[4]

Interact>>> ''')

	if fer == '1':
		ip = raw_input("Digite o IP: ")
		ports = []
		count = 0
		while count < 10:
			ports.append(int(raw_input("[*] Digite a Porta: ")))
			count += 1
		for port in ports:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(0.05)
			code = client.connect_ex((ip, port))
			if code ==0:
				print (str(port) + " -=> Porta aberta!")
				print("")
			else:
				print(str(port) + " -=> Porta Fechada!")
				print("")
		print("\n[*] Scan Finalizado!")




