try:
    a = int(input("give me a number pls "))
    b = int(input("give me another number pls "))
except ValueError:
    print("one of the numbers was invalid")
    exit(1) #you need this to avoid the error or move the else if string in between the try/except

if a > b:
    print(a, ">", b)
elif a < b:
    print(a, "<", b)
else:
    print(a, "=", b)

