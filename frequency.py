name = input("enter any sting : ")
d={}

for i in name:
	if i in d:
		d[i]=d[i]+1
	else: 
		d[i]=1

l=d.keys()

for i in l:
	print(i," ",d[i])


