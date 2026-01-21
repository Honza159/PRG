x="aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž "
a=input("Zadej frázi: ").lower()
b=int(input("Zadej posun: "))
c=""
d=""
for i in range(len(a)):
    for j in range(len(x)):
        if a[i] == x[j]:
            c+= x[j+b]
            d+= x[j-b]
            break
print("Zašifrováno: ",c)
print("Dešifrováno: ",d)