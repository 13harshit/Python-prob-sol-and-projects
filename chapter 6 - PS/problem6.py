# Ex = 90 - 100
# A = 80 - 90
# B = 70 - 80
# C = 60 - 70
# D = 50 - 60
# F = 50

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Your grade is Ex")
elif marks >= 80:
    print("Your grade is A")
elif marks >= 70:
    print("Your grade is B")
elif marks >= 60:
    print("Your grade is C")   
elif marks >= 50:
    print("Your grade is D")
else:
    print("Your grade is F")
