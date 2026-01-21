def palindrom():
    slovo = input("Zadej slovo: ")
    if slovo == slovo[::-1]: print("Je to palindrom")
    else:  print("Není to palindrom")
palindrom()

def factorial():
    a = 0
    for i in range(1,5):
        a += i*5
factorial()
