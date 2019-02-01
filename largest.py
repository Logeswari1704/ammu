a,b,c=input().split()
if(a>(b and c)):
	print(a)
elif(b>(a and c)):
	print(b)
else:
	print(c)
