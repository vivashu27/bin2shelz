import os
import re

binname=input("Enter the binary file name:\n")

cmd=f"hexdump {binname}  | cut -d  \" \" -f 2-8 | sed  '$s/.*//' > out.txt"
os.system(cmd)

f=open("out.txt","r")
counter=1
shellcode=""
comb=""

raw=str(f.read())
hex=re.sub("\s+","",raw)

#print(hex)

for i in hex:
	if counter%2==0:
		shellcode+='\\x'+str(comb)
		comb=""
	comb+=str(i)
	counter+=1

print("\n\n")
print(shellcode)
f.close()
os.system("rm out.txt")
