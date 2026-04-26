# Validate the quality and correctness of passwords
# must not be empty
#must be at least 1 UpperCase
# must included at least 1 lowercase
#  must not be same as the email
# must not contain any spaces
# must start and end with a letter or digit
Password = 'Aham@123'
Email = 'aham@123'
# must not be empty
if len(Password) == 0:
    print('password is invalid')
#must be at least 1 UpperCase
elif not any(c.isupper() for c in Password):
    print('Password is invalid')
# must included at least 1 lowercase
elif not any(c.islower()for c in Password):
    print('password is valid')
#  must not be same as the email
elif Password == Email:
    print('password can not be same as email')
# must not contain any spaces
elif ' ' in Password:
    print('password is invalid')
# must start and end with a letter or digit
elif not Password[0].isalnum() or Password[-1].isalnum():
    print('Not valid')
else:
    print('password is valid') 