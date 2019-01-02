from turtle import *

def flip(n):
    final= ''
    for elem in n:
        if elem == '0':
            final += '1'
        else:
            final += '0'
    return final

def sequence(number):
    sequence = '0'
    for n in range(number):
        sequence = sequence +'0' + palindrome(flip(sequence))
    return(str(sequence))

def palindrome(string):
    return string[::-1] 

turtle = Turtle()

def dragon_curve(sequence, length):
    turtle.left(90)
    speed = 'fastest'
    for elem in sequence:
        if elem == '0':
            turtle.right(90)
            turtle.forward(length)
        else:
            turtle.left(90)
            turtle.forward(length)

    
dragon_curve(sequence(10), 4)
