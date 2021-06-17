#factorial of number without recursion
#n!=n*(n-1)!
#3!=1*2*3=6

# n=int(input("Enter number:"))
# fact=1

# if n<0:
#     print("you Enter invalid input")
# elif n==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,n+1):
#         fact=fact*i
#     print(f"Factorial of {n} is {fact}")

#factorial of number with recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

num=int(input("Enter number:"))
f=fact(num)
print(f"Factorial of {num} is {f}")