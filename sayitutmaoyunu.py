import random
sayi=random.randint(0,100)
cvp=int(input("tuttuğum sayıyı tahmin et"))
while (sayi!=cvp):
    if (sayi<cvp):
        print("azalt")
        cvp=int(input("tekrar dene"))
    elif (sayi>cvp):
        print("artır")
        cvp = int(input("tekrar dene"))
print("doğru")
