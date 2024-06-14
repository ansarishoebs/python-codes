result = True
balance = 1000
password=input("enter 11111 IF YOU ARE FIRST USER : ")
if password == "11111":
	while result:
		options=input("select any one\n1-> press < W > for withdraw \n2-> press < D > for deposit \n3-> press < CPW > for change password \n4-> change password\n5-> press 0 for exit\n")
		print(options)
		if options == 'W' or options == 'w':
			print("your total balance is : ",balance)
			amt=input("enter the amount to be withdraw :")
			amt=int(amt)
			if amt > balance :
				print("you have insufficient amount ")
			else:
				balance=balance-amt;
				print("amount to be debited from your account")
				print("Total Balance : ",balance)
		elif options == 'D' or options == 'd':
			amt1=input("Enter Amount To Be Deposit : ")
			amt1=int(amt1)
			balance=balance+amt1
			print("Total Balance : ",balance)
		elif options == 'CPW' or options == 'cpw':
			newpass=input("Enter the new password : ")
			ch=input("for confirm yes/no : ")
			if ch == 'yes' or ch =='y':
				password=newpass
				print("Your password is Changed Successfully")
				pr = input("show new password press yes : ")
				if pr == 'yes' or pr == 'y':
					print(password)
			else:
				print("Thank you")
		elif options == '0':
			result=False
else:
	print("WRONG PASSWORD IF YOU ARE FIRST USER ENTER 11111")
