# exercise №4
#x0=a,x1=b,x2=c
a=0
b=9
c=9
d=0
i=0
S=0
n=int(input("Введіть n:"))
while 3<=i<=n:
    d=c+b+a
    S=d
    b=a
    c=b
    d=c
    i=i+1
print(S)



