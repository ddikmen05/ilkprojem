x=int(input("sayı girin :"))
a=0
b=x/2
while True :
    a=(b+x/b)/2
    if (b==a):
        break
    else:
        b=a

print(a)
