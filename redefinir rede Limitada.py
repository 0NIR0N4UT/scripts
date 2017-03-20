import os
import time

print("\nFeito Pelo Programador Adriel Freud\n   [*]_Redefinicao de rede_[*]")
print("\n")

sistema = raw_input("Digite seu Sistema Win\Unix: ")

if sistema == 'Win':
	if True:
		os.system("ipconfig /release")
		time.sleep(5)
		os.system("ipconfig /renew")
		print("Finish...!")

elif sistema == 'Unix':
	if True:
		os.system("ifconfig /release")
		time.sleep(5)
		os.system("ifconfig /renew")
		print("Finish...!")
