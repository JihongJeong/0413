Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def tempchange():
	print("Which temperature is it? : \n")
	print("1. Celsius \t 2. Fahrenheit")
	a = input()
	if a=="1":
		print("What temperature is it? : ")
		t = input()
		print(int(t)*(9/5)+32)
	else:
		print("What temperature is it? : ")
		t = input()
		print((int(t)-32)*(5/9))

	
>>> tempchange()
Which temperature is it? : 

1. Celsius 	 2. Fahrenheit
1
What temperature is it? : 
50
122.0
>>> tempchange()
Which temperature is it? : 

1. Celsius 	 2. Fahrenheit
2
What temperature is it? : 
50
10.0
>>> L = [1, 2, 3, 5, 9, 31, 28, 91]
>>> oddnum = 0
>>> evennum = 0
>>> for i in range(len(L)):
	if L[i]%2==0:
		evennum += 1
	else:
		oddnum += 1

	
>>> oddnum
6
>>> evennum
2
>>> check = [0]
>>> for i in range(1, 100):
	check = check + [0]

	
>>> for i in range(2, 100):
	if check[i]==0:
		for j in range(i, 100):
			if j%i==0:
				check[j] = 1

				
>>> check1 = [0]
>>> for i in range(1, 100):
	check1 = check1 + [0]

	
>>> for i in range(2, 100):
	if check[i]==0:
		for j in range(i+1, 100):
			if j%i==0:
				check[j] = 1

				
>>> primenum = 0
>>> for i in range(len(L)):
	if check[L[i]]==0:
		primenum += 1

		
>>> primenum
1
>>> primenum = 0
>>> for i in range(len(L)):
	if check1[L[i]]==0:
		primenum += 1

		
>>> primenum
8
>>> for i in range(10):
	print(check1[i])

	
0
0
0
0
0
0
0
0
0
0
>>> for i in range(2, 100):
	if check1[i]==0:
		for j in range(i+1, 100):
			if j%i==0:
				check1[j] = 1

				
>>> primenum = 0
>>> for i in range(len(L)):
	if check1[L[i]]==0:
		primenum += 1

		
>>> primenum
5
>>> for i in range(len(L)):
	if check1[L[i]]==0:
		print(L[i])

		
1
2
3
5
31
>>> 