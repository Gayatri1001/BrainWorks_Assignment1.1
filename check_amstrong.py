#If it is equal to the sum of cubes of its digits
#153 = 1x3 + 5x3 + 3x3 = 153

n=int(input("Enter number:"))

sum=0
temp=n

while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10

if n==sum:
    print(f"{n} is amstrong")
else:
    print(f"{n} is not amstrong")