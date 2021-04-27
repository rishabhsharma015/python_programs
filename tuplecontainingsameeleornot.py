t1=eval(input())
t2=eval(input())
t3=()
for i in t1:
	if i in t2:
		t3+=(i,)
if t3==t1:
       print("tuples containing same elements")
else:
	print("tuples not containing same elements")
	
#if t1!=t2:
#	print("They are not in same order")
#else:
#	print("They are in same order")


		

