Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> total_min = 1300
>>> total_hour = total_min/60
>>> total_time_representing = "Hour : "+str(total_hour)+" Min : "+str(total_min%60)
>>> print(total_time_representing)
Hour : 21.666666666666668 Min : 40
>>> total_time_representing = "Hour : "+str((int)total_hour)+" Min : "+str(total_min%60)
SyntaxError: invalid syntax
>>> total_hour = int(total_min/60)
>>> total_time_representing = "Hour : "+str(total_hour)+" Min : "+str(total_min%60)
>>> print(total_time_representing)
Hour : 21 Min : 40
>>> 