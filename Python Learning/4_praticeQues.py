#generate a random integer between 1 to 100 and check if the result is an even number 
import random
x = random.randint(1,100)
print(x)
if(x % 2 == 0):
    print('even')
else:
    print('odd')

# 2nd method 
num = random.randint(1,100)
print(num , 'number is ' , num%2 == 0)