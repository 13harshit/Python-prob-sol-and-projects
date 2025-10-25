sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))
total = sub1 + sub2 + sub3
percentage = (total / 300) * 100
if percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("Congratulations! You have passed.",percentage)
else:
    print("You have failed,try next years!",percentage)