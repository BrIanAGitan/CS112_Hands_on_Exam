numb = int(input("Enter conversion method: "))

if numb == 1 :
    dec1 = int(input("Enter a decimal number: "))
    print(format(dec1, "b"))
elif numb == 2 :
    dec1 = int(input("Enter a decimal number: "))
    print(format(dec1, "o"))
elif numb == 3 :
    dec1 = int(input("Enter a decimal number: "))
    print(format(dec1, "x"))
else:
    print("Invalid Input, Enter another number")

