# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:27:10 2017

@author: Cesar
"""

# Assigment 1 - 9.4

## 9.4 Write a program to read through the mbox-short.txt and figure out who 
## has the sent the greatest number of mail messages. The program looks for 'From '
## lines and takes the second word of those lines as the person who sent the mail. 
## The program creates a Python dictionary that maps the sender's mail address 
## to a count of the number of times they appear in the file. After the dictionary 
## is produced, the program reads through the dictionary using a maximum loop 
## to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = 0
emails = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    emails[words[1]] = emails.get(words[1],0) + 1
 
maxcount = None
maxword = None

for email,count in emails.items():
    if maxcount is None or maxcount < count:
        maxcount = count
        maxword = email

print(maxword,maxcount)