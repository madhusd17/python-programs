n=input("Enter the number:")
l=len(n)
sum=0
for i in n:
    x=int(i)  
    sqr=pow(x,l)
    sum+=sqr
if int(n)==sum:
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
