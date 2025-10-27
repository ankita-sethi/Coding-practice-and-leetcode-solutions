def reverseString(a1):
	a=list(a1)
	n=len(a)
	temp = ""
	if n>1:
		for i in range(n//2):
			temp=a[i]
			a[i]=a[n-i-1]
			a[n-i-1]=temp
			
	str1= ''.join(a)
	return str1

a1 = input("enter string ")
print(reverseString(a1))