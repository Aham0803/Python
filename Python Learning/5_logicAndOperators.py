email = ""
phone = "01456664"
userName = ""

# any() -> returns true if one value is true
print(any([email, phone, userName]))
# all() -> returns true if all values are true
print(all([email, phone, userName]))

#logical operations
print(not 3 > 2)

# in operator -> checks if value inside another value , like a string , list , tuple or other sequence
print('o' in 'python')
print('z' not in 'python')
print(3 in [1, 2 , 3])

# is operator -> checks if two variabkes refer to same obj in memory
x = ['a' , 'b' , 'c']
y = ['a' , 'b' , 'c'] 
print(x == y)
print(x is y)

x = 10
y = 10
print(x == y)
print(x is y)
