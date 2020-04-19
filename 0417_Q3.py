Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set1 = set(['rap', 'house', 'electronic music', 'rap'])
>>> set1
{'electronic music', 'house', 'rap'}
>>> A = [1, 2, 2, 1]
>>> b = set([1, 2, 2, 1])
>>> b
{1, 2}
>>> A
[1, 2, 2, 1]
>>> sum(A)
6
>>> sum(b)
3
>>> # sum(A) != sum(b)
>>> album_set1 = set(["Thriller", 'AC/DC', 'Back in Black
		  
SyntaxError: EOL while scanning string literal
>>> album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
>>> album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])
>>> album_set3 = album_set1.union(album_set2)
>>> album_set3
{'The Dark Side of the Moon', 'AC/DC', 'Thriller', 'Back in Black'}
>>> album_set1 == album_set3.intersection(album_set1)
True
>>> #albumset1 is subset of album_set3
>>> 