def f(x):
    return x**2+1

def fp(x):
    return 2*x

num =1
a = 3

while 1:
    print("try : ", num)
    print("(X, Y) : (", a,",", f(a),")")
    print("\n")
    x = a
    y = f(a)
    k = y-fp(a)*x
    a = (-1*k)/fp(a)
    num+=1
    if y<1.01:
        break

"""
the answer looks like this

try :  1
(X, Y) : ( 3 , 10 )


try :  2
(X, Y) : ( 1.3333333333333333 , 2.7777777777777777 )


try :  3
(X, Y) : ( 0.29166666666666663 , 1.0850694444444444 )


try :  4
(X, Y) : ( -1.5684523809523812 , 3.4600428713151934 )


try :  5
(X, Y) : ( -0.46544061172856255 , 1.2166349630462585 )


try :  6
(X, Y) : ( 0.8415306026309832 , 1.7081737551644658 )


try :  7
(X, Y) : ( -0.1733901559391667 , 1.0300641461766085 )


try :  8
(X, Y) : ( 2.796974974068567 , 8.823069005565863 )


try :  9
(X, Y) : ( 1.2197229272382104 , 2.4877240192305488 )


try :  10
(X, Y) : ( 0.1999322995161248 , 1.0399729243898055 )


try :  11
(X, Y) : ( -2.400880392847098 , 6.764226660757635 )


try :  12
(X, Y) : ( -0.9921832580564227 , 1.9844276175674578 )


try :  13
(X, Y) : ( 0.007847533359435319 , 1.0000615837798275 )

whith Newton method, I can find the solution in 13time,
that is more faster than assignment's code

"""
