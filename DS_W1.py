# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 17:37:23 2017

@author: Cesar
"""
## Chapter 6 
## Excercise 5
text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
num = float(text[pos:len(text)])
print(num)
