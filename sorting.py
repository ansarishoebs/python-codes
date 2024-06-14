
#>>>>>>>>>>>  input the various words separatd by , 	<<<<<<<<<<<<<<<<<<<<<<<<<<#


name=input("enter the name separated by ','  : ")


l=name.split(',')
#print(l)
l1=sorted(l)

for i in l1:
	print(i,end=" ")
print()
