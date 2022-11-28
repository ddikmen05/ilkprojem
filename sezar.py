alfabe = "abcçdefgğhıijklmnoöprsştoövyz"

#print(alfabe.index("d"))
#print(alfabe[28])
#print(len(alfabe))

text=input("şifrelenecek metni girin:")
shift=int(input("şifreyi girin:"))

encrypted_text=""

for  i in range(len(text)):
    enc_idx=(alfabe.index(text[i])+ shift)%29
    encrypted_text=encrypted_text+alfabe[enc_idx]

print("şifrelenmiş metin:",encrypted_text)
