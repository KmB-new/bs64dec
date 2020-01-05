uimport base64
from time import sleep
from sys import exit
print "        [ base64 mass crack ]"
print " [ made with full of <3 by LOoLzeC ]\n"
string = raw_input('- string list> ')
print "+ cracking ..."
print "-"*40
try:
	o=open(string).readlines()
except:
	print "- gagal buka list nya"
	exit()
s=[]
j=[]
berhasil=open('berhasil.txt','w')
for k in o:
	try:
		print "+ result -> ",base64.b64decode(k.split('\n')[0])
		ber=base64.b64decode(k.split('\n')[0])
		j.append(ber)
		sleep(00.01)
	except:
		print "- incorrect padding."
		s.append(k)
		sleep(00.01)
print "-"*40
for result in j:
	berhasil.write(result.split('\n')[0]+"\n")
berhasil.close()
print "+ total berhasil:",len(j)
print "+ output : berhasil.txt"
print "-"*40
print "- gagal:",len(s)
for t in s:
	print "- gagal:",t.replace('\n','')
print "-"*40
