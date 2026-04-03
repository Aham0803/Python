#Strings
#type()
name = "aham"
print(type(name))

#str()
age = 24
# print("your age is : " + age)  it will give error
print("your age is : " + str(age)) # it changes int to str only inside print function , outer of print it will always be int

#Math
#len()
password = "123a"
print(len(password))

#count(substring)
text = """
Python is easy
Python is powerful
"""
print(text.count("Python"))

#data transformation
#replace()
price = "1234,56"
print(price.replace(',' , '.'))

phone = "+49 (176) 123-4567"
print(phone.replace("+","00").replace(" ","").replace("(" , "").replace(")" , "").replace("-",""))

#Transformation
first_name = "aham"
last_name = "golash"
last_name = first_name + " " + last_name
print(last_name)

#f-Strings
name = "sam"
age = 34
is_student = False
print("my name is " + name + " , I am " + str(age) + " years old, and student status is " + str(is_student) + ".")
print(f"my name is {name} , I am {age} years old, and student status is {is_student}.")

print(f" 2+3 = {2+3}")
print(f"{{this is me}}")

#split() -> breaks a string into smaller parts
stamp = "2026-09-20 14:30"
print(stamp.split(" "))

#String Repetition
print("ha" * 3)

#Indexex & Slicing
text = "Python"
#Extract the first element
print(text[0])
print(text[-6])
#Extract the last character
print(text[5])
print(text[-1])
#Extract h
print(text[3])

date = "2026-09-20"
#Extract the year
print(date[0:4])
print(date[:4])
#Extract the month
print(date[5:7])

#Data Cleaning
#lstrip()
text = " Engineering".lstrip()
print(text)
write = "Abcdefg  ".rstrip()
print(write)
read = " abcdef ".strip()
print(read)
hash = "######abs###".strip("#")
print(hash)

#imp key
nam = " Enginnering"
print(len(nam))
print(len(nam.strip()))

no_of_spaces = len(nam) - len(nam.strip())
print("number of spaces",no_of_spaces)
is_clean = len(nam) == len(nam.strip())
print("is my data clean ?",is_clean)

#case conversion
text = "python PROGRAMMING"
print(text.lower())

search = "EMAIL ".lower().strip()
data = "  emaIL".lower().strip()
print(search == data)

challenge = "968-Maria, ( D@t@ Enginner );; 27y  "
#name: maria | role: data enginner | age: 27
name = challenge[4:9]
role = challenge[13:26].lower().replace("@" , "a")
age = challenge[-5:-3]

print("name: " , name , " | role: " , role ," | age: " , age)

#Search
phone = "+49-176-12345"
#startwith()
print(phone.startswith("+49"))
email = "ahamgolash9340@gmail.com"
#endswith()
print(email.endswith("gmail.com"))
# in
print("@" in email)
#find()
phone1 = "+48-176-12345"
print(phone1.find("-"))
print(phone1[phone1.find("-")+1 :])

#validation
#isalpha()
country = "USA"
print(country.isalpha())
#isnumeric()
phone = "01761234587"
print(phone.isnumeric())
