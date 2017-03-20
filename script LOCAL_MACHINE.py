import os
import time

print ('''
*******************************************************************
** SEJA BEN-VINDO USUARIO EU SOU O SCRIPT CRIADO PELO (>Adriel<) **
**\n [*]	[*]		[*]		[*]			[*]	  [*]		[*]	     **
*******************************************************************
\n''')
try:
	os.system("mkdir CopiasRun")
	print("[-]\n Criado pasta")
	print("\n")
	os.system('REG EXPORT "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" "CopiasRun"\HKLM-Run.reg') 
	os.system('REG EXPORT "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" "CopiasRun"\HKCU-Run.reg')
	print("\nCOPIAS DA CHAVE ( HKEY_LOCAL_MACHINE ) DA PASTA ( Run )") 
	print("\n==============================================================")
	print("\n( * VERIFICACAO DE CONEXOES * )")
	os.system("time /t")
	print("\n______________\n")
	os.system("date /t")
	print('''
	==================================================================
	== [ENDERECO LOCAL] [ENDERECO EXTERNO [IP] [PORTAS] [CONECXOES] ==
	==================================================================
	''')
	os.system("netstat -n")
	print('''\n
	======================================================================
	==    EXECUTAVEIS RESPONSAVEIS PELA CONECXAO COM O COMPUTADOR       ==
	======================================================================
	''')
	print("[+] Fim da Verificacao!\n Adriel SCRIPTS )")
	print("\n\n[+] Abrindo Gerenciador de Tarefas!")
	os.system("start taskmgr.exe")

except Exception as e:
	print("[-] Error: ", e)
	print("[*] Tente novamente!")
