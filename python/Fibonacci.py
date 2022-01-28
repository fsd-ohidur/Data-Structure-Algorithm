numbers=10

## Solution 1
#i,j=0,1
#print(i)
#for number in range(numbers-1):
#    print(j)
#    i,j=j,i+j

## Solution 2
def fibonacci(n):
    if n<2:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

for number in range(numbers):
    print(fibonacci(number))