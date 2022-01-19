import os

print("SSH AUTOMATION")
print("Tool By YATHARTHGEEK")

print("")

print("Hint : Type Y/N to enable/disable SSH Connection")
print("")
print("")
bash= input("[SSH-AUTO]>>  ")

if bash=="y":
	print("Enabling SSH Connection")
	os.system("service ssh start")
	

if bash=="n":
	print("ThankYou")
	os.system("service ssh stop")

if bash=="connect":
	inf= input("Enter Username : ")
	ipaddr = input("Enter IP Address : ")
	iport = input("Enter Port : ")
	code = "ssh"+" "+inf+"@"+ipaddr+" "+"-p"+" "+iport
	os.system(code)
