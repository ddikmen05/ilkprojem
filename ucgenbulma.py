a=int(input("birinci kenarın uzunluğunu söyle"))
b=int(input("iknci kenarın uzunluğunu söyle"))
c=int(input("üçüncü kenarın uzunluğunu söyle"))
if abs(a-b)<c and abs(a+b)>c:
    print("üçgen olur")
else:
    print("üçgen olmaz")
