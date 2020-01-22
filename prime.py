n = int(input("enter a number"))
i=2
c=0
while(i<=n/2):
    if(n%i==0):
        c=c+1
        break
    i=i+1
if(c==0 and n!=1):
    print(n,"is  prime")
else:
    print(n,"is not prime")