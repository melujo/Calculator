import arith_tools

from typing import List
from functools import reduce
from operator import add

'''
Calculates the sum of a and b.
Only supports positive integers.
'''
def sum(a, b):
    r = 0                                     # Result
    c = 0                                     # Carry
    a = int(a)
    b = int(b)
    length_a = arith_tools.get_number_length(a)     # Get length of number a
    length_b = arith_tools.get_number_length(b)     # Get length of number b
    max_length = max(length_a, length_b)              # Calculate maximum a if a > b, else b
    
    if a < 0 and b > 0:
        r = sub(a*(-1),b)
        r *= -1
    elif b < 0:
        r = sub(a,b*(-1))
    else:
        # Implement algorithm
        list_a = [int(i) for i in str(a)]
        list_b = [int(i) for i in str(b)]
        if arith_tools.longest(length_a,length_b) == length_a:
            while len(list_b) != len(list_a):
                list_b.insert(0,0)
        else:
            while len(list_a) != len(list_b):
                list_a.insert(0,0)
        list_r = []
        for i in range(max_length):
            minus_i = (i * (-1)) - 1
            tempR = c + list_a[minus_i] + list_b[minus_i]
            list_r.append(tempR % 10)
            c = tempR // 10
        if c > 0:
            list_r.append(c)
        list_r	= list_r[::-1]
        r = arith_tools.list_to_str(list_r)
    return r

'''
Calculates the subtraction of a and b.
Only supports positive integers.
'''
def sub(a, b):
    r = 0                                           # Result
    c = 0                                           # Borrow
    a = int(a)
    b = int(b)
    s = 1                                           # Sign is positive
    if b > a:
        s = -1

    length_a = arith_tools.get_number_length(a)     # Get length of number a
    length_b = arith_tools.get_number_length(b)     # Get length of number b
    max_length = max(length_a, length_b)            # Calculate maximum a if a > b, else b
    

    
    # Implement algorithm
    list_a = [int(i) for i in str(a)]
    list_b = [int(i) for i in str(b)]
    if arith_tools.longest(length_a,length_b) == length_a:
        while len(list_b) != len(list_a):
            list_b.insert(0,0)
    else:
        while len(list_a) != len(list_b):
            list_a.insert(0,0)
    list_r = []
    for i in range(max_length):
        minus_i = (i * (-1)) - 1
        if s == 1:
            digit = list_a[minus_i] - list_b[minus_i] - c
        elif s == -1:
            digit = list_b[minus_i] - list_a[minus_i] - c
        if digit < 0 and i != max_length - 1:
            digit += 10
            c = 1
        else:
            c = 0
        list_r.append(digit)
    list_r = list_r[::-1]
    r = int(arith_tools.list_to_str(list_r))
    return r * s                                # Note the sign

'''
Calculates the multiplication of a and b.
Only supports positive integers.
'''
def multiply(a, b):
    r = 0                                        # Result
    a = int(a)
    b = int(b)
    if a > b:
        large = a
        small = b
    else:
        large = b
        small = a
    # Implement algorithm
    for i in range(small):
        r = int(sum(r,large))
    return r

'''
Calculates the division of a and b.
Only supports positive integers.
'''
def divide(a, b):                       
    i = 0                                     # Result
    # Implement algorithm
    while a > 0:

        a = int(sub(a,b))
        i = sum(i,1)
        if a < 0:
            i = sub(i,1)
            
            break
    return i

'''
MANDATORY WEEK 5
'''

'''
Calculates the power of a and b.
Only supports positive integers.
'''
def power(a, b):
    r = 1                                     # Result
    # Implement algorithm
    for i in range(b):
        r = int(multiply(r, a))
    return r

'''
Calculates the square root of a.
Only supports positive integers.
'''
def sqrt(a):
    if a <= 1:                                      # Early escape
        return a
    
    i = 1                                           # Increments
    r = 1                                           # Result of multiplication with i
    
    # Implement algorithm
    for i in range(sub(a,1)):
        if pow(i,2) == a:
            r = i 
            break
        elif pow(i,2) > a:
            r = sub(i,1)
            break
    return r                                # Subtract one from increment

'''
Calculates the modulo of a and b.
Only supports positive integers.
'''
def mod(a, b):
    return int(sub(a, multiply(divide(a, b), b)))        # Calculate a - ((a / b) * b)

'''
Calculates the gcd of a and b.
Only supports positive integers.
'''
def gcd(a, b):
    if b == 0:
        r = a
    else:
        r = gcd(b,mod(a,b))
    return r

'''
Calculates the lcm of a two integers.
Only supports positive integers.
'''
def lcm(a, b):
    return int(divide(multiply(a,b),gcd(a, b)))

'''
Converts a binary string to a decimal integer.
'''
def bin(a : str):
    r = 0
    lis = list(a)
    count = 0    
    for i in lis:
        if i == '1':
            r = sum(r,power(2,int(sub(sub(len(a),1),count))))
        count = sum(count,1)

    return str(r)