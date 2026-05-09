# check whether any filename appears more than once
# print "duplicate found" if a duplicate exists, otherwise print "all files are unq"

file_list = ['report.csv' , 'data.xlsx', 'summary.docx' , 'report.csv' , 'data.csv']

seen = []
for file in file_list:
    if file in seen:
        print("duplicate found")
        break
    seen.append(file)
else:
    print("all files are unq")

print("h")
