print("hai")
try:    
    x=int(input("enter x value: "))
    y=int(input("enter y value: "))
    try:
        z=x/y
        print(z)
    except ValueError:
        print("Please enter integers only")
except NameError:
    print("hai")
print("bye")
