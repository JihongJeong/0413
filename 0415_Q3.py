Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple_Genre = ((0, "Pop"), (1, "Rock"), (2, "Soul"), (3, "Hard Rock"), (4, "Soft Rock"), (5, "R&B"), (6, "Prograessive rock"), (7, "Disco"))
>>> def{
	
SyntaxError: invalid syntax
>>> def
SyntaxError: invalid syntax
>>> def:
	
SyntaxError: invalid syntax
>>> def find():
	print("What is number of : ")
	a = input()
	if a == "Pop":
		print("number of "+a+" is 0")
	elif a == "Rock":
		print("number of " + a + " is 1")
	elif a == "Soul":
		print("number of " + a + " is 2")
	elif a == "Hard Rock":
		print("number of " + a + " is 3")
	elif a == "Soft Rock":
		print("number of " + a + " is 4")
	elif a == "R&B":
		print("number of " + a + " is 5")
	elif a == "Prograessive rock":
		print("number of " + a + " is 6")
	elif a == "Disco":
		print("number of " + a + " is 7")
	else:
		print("there is no number of "+a)

		
>>> find()
What is number of : 
R&B
number of R&B is 5
>>> find()
What is number of : 
K-pop
there is no number of K-pop
>>> 