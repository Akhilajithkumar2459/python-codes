# -*- coding: utf-8 -*-
"""calculator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZWZ9u6_E2zI5epSC4iRVRE-uJfo0ywwC
"""

def add(a,b):
  answer = a+b
  print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a,b):
  answer = a-b
  print(str(a) + "-" + str(b) + "=" + str(answer))

def mul(a,b):
  answer = a*b
  print(str(a) + "×" + str(b) + "=" + str(answer))
def div(a,b):
  answer = a/b
  print(str(a) + "÷" + str(b) + "=" + str(answer))


print("A.Addition")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")

choice=input("Enter the choice")

if choice=="A" or choice=="a":
  print("Addition")
  a=int(input("Enter the first number"))
  b=int(input("Enter the first number"))
  add(a,b)
elif choice=="B" or choice=="b":
  print("Subtraction")
  a=int(input("Enter the first number"))
  b=int(input("Enter the first number"))
  sub(a,b)
elif choice=="C" or choice=="c":
  print("Multiplication")
  a=int(input("Enter the first number"))
  b=int(input("Enter the first number"))
  mul(a,b)
elif choice=="D" or choice=="d":
  print("Division")
  a=int(input("Enter the first number"))
  b=int(input("Enter the first number"))
  div(a,b)
else:
  print("Wrong Choice please select the right choice")

