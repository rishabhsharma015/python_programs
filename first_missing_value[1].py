# You are given a list of positive and negetive integers , your task is to find out the first missing positive integer.

l1=[]
l=list(map(int,input().split()))
for i in range(len(l)):
	if l[i]>0:
		l1.append(l[i])
for j in range(min(l1),max(l1)+1):
	if j not in l1:
		print("First missing positive number:",j)
		break


