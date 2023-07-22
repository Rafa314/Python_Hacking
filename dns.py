
from socket import gethostbyname, gaierror
print("============================================================================================================================")
print("==== ALGORITMO PARA ENUMERAÇÃO DNS(Domain Name System - Sistema de Nome de Domínio) ====")
print("============================================================================================================================")
dominio = input("Digite o nome do seu alvo: ")
brute = ["ns1","ns2","ns3","ns4","www","ftp","intranet","mail"]


with open("resultado.txt", "w") as arquivo:
    for nome in brute: 
        dns = nome + "." + dominio
        try:
            print(dns + ": " + gethostbyname(dns))
            arquivo.writelines(dns + ": " + gethostbyname(dns) + "\n")
        except gaierror:
            pass 

