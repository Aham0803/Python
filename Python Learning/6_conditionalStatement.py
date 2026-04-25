score = 20
Submitted_project = True
if score >= 100:
    if Submitted_project:
        print("A+")
    else:
        print("A")
elif score > 50:
    print("c")
else:
    print("B")

grade = "A" if score >=  90 else "F"
print(grade)

print( "A" if score >=  90 else "F")