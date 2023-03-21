# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline

A = int(input())

array = []

for _ in range(A):
	temp = int(input())
	
	array.append(temp)

cut = 1

maxnum = array[-1]

for i in range(A-1,-1,-1):
	if maxnum < array[i-1]:
		cut += 1
		maxnum = max(array[i-1], array[i])
		
print(cut)
	

