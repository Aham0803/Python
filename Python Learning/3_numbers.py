import math #for floor()
import random
#Types
x = 5
y = 5.7
z = 2 + 3j
print(type(x))
print(type(y))
print(type(z))

x = "24"
print(type(x))
x = int(x)
print(type(x))

#complex(real , imag) -> creates a complex number using real and imaginary parts
x = 3 #real
y = 4 #img
print(complex(x,y))

#Math Operator
print(7/2)
print(7//2) #floor devision -> it divides two numbers and rounds down  
print(2 ** 3) #exponentiation -> it raises a number to the power of another number 

#Rounding
print(abs(2-10)) #abs(value) -> returns the absolute (non-negative) value of a number 

#rounding Numbers 
price = 35.54879865
print(round(price))
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))

#random() -> returns a random float btw 0.0 and 1.0
print(random.random())
print(random.randint(1,6))

#Validation
#is_integer() -> checks if a float has no decimal part (is a whole number)
x = 7.0
print(x.is_integer())

#isinstance(value, type) -> checks if a value to a certain data types

x = 70
print(isinstance(x , int)) #isinstance(value,type) -> checks if a value belongs to certain data type 
  
