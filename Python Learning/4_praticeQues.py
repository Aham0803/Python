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

#Allow access only if the user is logged in or they are guest but they must not banned 
is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned)

