a=int(input("enter a 1 number"))
b=int(input("enter a 2 number"))
try:
    if a%2==0:
        print("correct")
except Exception:
    print("handle")