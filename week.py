week=['Monday','Tuesday','Wednesday','Thursday','Friday']
weekend=['Saturday','Sunday']
s=input(" ")
for i in range(5):
	if(s==week[i]):
		print("no")
for i in range(2):
	if(s==weekend[i]):
		print("yes")
