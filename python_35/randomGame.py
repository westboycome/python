#!.usr/bin/python
import random
import sys
import os
secret = random.randint(1, 9)
temp = input("输入一个数字\n")
try:
    guess = int(temp)
except:
    print("dd")
    os._exit(0)
count = 0
while guess != secret:
    if count == 0 and guess > secret:
        print("大")
    if count == 0 and guess < secret:
        print("小")
    
    temp = input("new number \n")
    count +=1
    if count > 2:
        print("dsd")
        break
