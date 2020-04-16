Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1 = "ABCDFE"
>>> print(s1[3])
D
>>> print(s1[2:4])
CD
>>> print(s1.find('C'))
2
>>> print(s1.count('E'))
1
>>> print(s1.lower())
abcdfe
>>> print(string.upper())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(string.upper())
NameError: name 'string' is not defined
>>> print(s1.upper())
ABCDFE
>>> print(s1.replace('ABC', 'CDE'))
CDEDFE
>>> 