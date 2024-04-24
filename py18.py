import  math  
x = str(input('Cfare kufize mungon(a/b/c):'))

if x == "c":
    a = float(input("Vleren e a: "))
    b = float(input("Vleren e b: "))
    c = math.sqrt(a ** 2 + b ** 2)
    print(c)
elif x == "a":
    b = float(input("Vleren e b: "))
    c = float(input("Vleren e c: "))
    a = math.sqrt(c ** 2 - b ** 2)
    print(a)
elif x == "b":
    a = float(input("Vleren e a: "))
    c = float(input("Vleren e c: "))
    b = math.sqrt(c ** 2 - a ** 2)
    print(b)

else:
    print("Wrong!")
