# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a, tick = map(int, input().split(' '))
num = input().split(' ')

cnt = 0

for i in range(0, a-1):
	if((int(num[i+1]) - int(num[i])) >  tick):
		cnt = 0
		
	else:
		cnt += 1
print(cnt + 1)
