#Python Program to find largest element in an array

# #1.using inbuit function max
# -----------------------------

# arr=[10,20,30,40,50]
# output=max(arr)
# print(output)

#2.

def largest(arr,n):

	max = arr[0]

	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max

arr = [10,50,20,30,40]
n = len(arr)
output = largest(arr,n)
print (f"The largest number is {output}")


