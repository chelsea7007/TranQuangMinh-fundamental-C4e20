# Finish CRUD exercise in class, simulate a clothes shop
a = True
while a:
    CRUD = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    items = ["T-Shirts", "Sweater"]
    if CRUD == "R": 
        print ("Our items: ", end="")
        print(*items, sep=", ")
    elif CRUD == "C":
        ni = input("Enter new item: ") #enter Jeans
        items.append(ni)
        print("Our items: ", end="")
        print(*items, sep=", ")
    elif CRUD == "U":
        items.append(ni)
        p = int(input("Update position? ")) #enter 2
        b = input("New item? ") #enter skirt
        items[p-1] = b
        print("Our items: ", end="")
        print(*items, sep=", ")
    else:
        items.append(ni)
        items[1] = b
        d = int(input("Delete position? "))
        del items[d-1]
        print(*items, sep=", ")