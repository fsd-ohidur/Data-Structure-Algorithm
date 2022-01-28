#write a programme that print 1 to 100, but number multiplited by 3 print fizz,
#by 5 print Buzz, by both 3 & 5 print fizzbuzz

for i in range(100):
    j=i+1
    
    if j%3==0 and j%5==0:
        print('FizzBuzz')
    elif j%3==0:
        print('Fizz')
    elif j%5==0:
        print('Buzz')
    else:
        print(j)