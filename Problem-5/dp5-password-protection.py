def locked():
	found = 0
	username = input("Enter your username: ")
	user = open('username.txt', 'r')
	userlist = user.read().split("\n")
	user.close()
	for line in userlist:
		if username in line:
			found = 1;
			num = userlist.index(line)
			break
	if found == 0:
		print("You are not what we are looking for.")
		locked()
	else:
		checkPass(username, num)
			
def checkPass(username, num):
	print("Welcome " + username + ", ")
	password = input("Enter your Password: ")
	pass1 = open('password.txt', 'r')
	passlist1 = pass1.read().split("\n")
	pass1.close()
	if password == passlist1[num]:
		print("You are a candidate for human sacrifice.")
	else:
		print("Enter the right password")
		checkPass()

		

locked()