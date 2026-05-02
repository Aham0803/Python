# check for missing number 
names = ['kamara' , 'tuba' , None , 'monika']

for name in names:
    if name is None:
        print("Found a missing  name")
        break
else:
    print("all names are avl")


# check if all files are csv files
files = ['data.csv' , 'report.pdf' , 'report2.csv']

for file in files:
    if not file.endswith('.csv'):
        print(f'{file} is not a csv')
        break

else:
    print("all files are csv")