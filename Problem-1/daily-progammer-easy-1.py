name = input("Enter your name: ")
age = input("Enter your age: ")
reddit = input("What is your reddit username: ")

print ("Your name is %s, you are %s years old and your username is %s." % (name, age, reddit))

with open('file.txt', 'w+') as f:
	f.writelines(name + ' ' + age + ' ' + reddit)