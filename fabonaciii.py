#generate fabonacii without recursion
#fabonacii series --->0 1 1 2 3 5 8 13 21 34.......

def fabo(n):
    if n<0:
        print("Invalid Input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fabo(n-1)+fabo(n-2)
    
num=int(input("Enter number:"))
f=fabo(num)
print(f)



