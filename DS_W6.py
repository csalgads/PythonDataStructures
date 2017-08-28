# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:56:36 2017

@author: Cesar
"""

# Assigment 
## 10.2 Write a program to read through the mbox-short.txt and figure out the 
## distribution by hour of the day for each of the messages. You can pull the 
## hour out from the 'From ' line by finding the time and then splitting the 
## string a second time using a colon.
## From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
## Once you have accumulated the counts for each hour, print out the counts, 
## sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = 0

times = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    times.append(words[5])
hours = dict()
for time in times:
    hour = time.split(':')
    hours[hour[0]] = hours.get(hour[0],0) + 1

answer = list()    
for key,val in hours.items():
    newtup = (key,val)
    answer.append(newtup)
answer = sorted(answer)
for key,val in answer:
    print(key,val)
    
    
    
    
    
    
    