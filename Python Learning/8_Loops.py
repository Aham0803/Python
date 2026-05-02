items = (1 , 2 , 3 ,4 ,5)
for i in (items):
    print(f"Round: {i}")

items = [1,2,3,4,'hi']
for item in (items):
    print(f"Round : {item}")

items = "Python"
for item in items:
    print(f"Round : {item}")

# Range(start,stop,step)
for item in range(5):
    print(f"Round : {item}")

scores = [80, 50 , 60 , 75]
total = 0
for score in scores:
    total += score
    print("Current Total :" , total)
print("Final Total :" , total)

#ques -> clean the following data
files = ['  Report.csv  ', 'Data.csv  ' , '  final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt' , '.csv')
    print(file)

#ques -> print the 7-times table from 1 to 10 using for loop
for table in range(1,11):
    print(f'7 * {table} = {7*table}')

#ques -> 
# *
# **
# ***
# ****
# *****

for start in range(1,6):
    print("*" * start)

#break statemrnt
names = ['john' , 'maria' ,'','kumar']
for name in names :
    if name == '':
        print('empty value detected!')
        break
    print(f'name ={name}')

# continue statement -> it skips one loop cycle without stoppping the loop
names = ['john' , 'maria' ,'','kumar']
for name in names :
    if name == '':
        print('empty value detected!')
        continue
    print(f'name ={name}')

# pass -> it is a placeholder where nothing happens
names = ['john' , 'maria' ,'','kumar']
for name in names :
    if name == '':
        pass #todo handle empty value
    print(f'name ={name}')

# skips weekends in calender loop
days = ['mon' , 'sun' , 'wed' , 'tue']
for day in days:
    if day in ['sat' , 'sun']:
        continue
    else:
        print(f'workday : {day}') 

# scan email to block unsafe data from entering your system
emails = [
    'data@gmail.com',
    'baraa@outlook.de',
    'Drop Table users;'
    'maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print('sql injection: hacker attack')
        break
    print(f' Processing email: {email}')

print("email")

# else in loop -> runs a block of code only if loop finishes naturally
items = [1 , 3 ,4 , 7]
for i in items:
    if i%2 == 0:
        print("even number is found" ,i)
        break
else:
    print("All no are odd")
