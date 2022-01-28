str='Bangladesh'
def reverseString(str):
    newstr=''
    for i in range(len(str)-1,-1,-1):
        newstr+=str[i]
    return newstr
    
print(reverseString(str))

# python function
print(str[::-1])