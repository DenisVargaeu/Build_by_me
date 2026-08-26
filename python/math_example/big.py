
# not working properly, need to fix it
a = 4
b = 10
c = 11
a1 = 0
a2 = 0
a3 = 0


def check2 ():
    global a1, a2, a3
    if a1 == 0 and a2 == 0:
        print (f"Number {a3} is the smallest number")
    elif a2 == 0 and a3 == 0:
        print (f"Number {a1} is the smallest number")
    elif a1 == 0 and a3 == 0:
        print (f"Number {a2} is the smallest number")


def check3 ():
    global a1, a2, a3
    if a2 == 0:
        if a1 >= a3:
            print (f"Number {a1} is the second largest number")
        elif a3 >= a1:
            print (f"Number {a3} is the second largest number")
    elif a1 == 0:
        if a2 >= a3:
            print (f"Number {a2} is the second largest number")
        elif a3 >= a2:
            print (f"Number {a3} is the second largest number") 
    check2 ()


def check (a, b, c): 
    global a1, a2, a3
    if a >= b and a >= c:
        print (f"Number {a} is the largest number")
        a2 = a
    elif b >= a and b >= c:
        print (f"Number {b} is the largest number")
        a1 = b
    elif c >= a and c >= b:
        print (f"Number {c} is the largest number")
        a3 = c
    check3 ()



check (456, 10, 11)