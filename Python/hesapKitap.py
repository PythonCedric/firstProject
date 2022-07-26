a = int(input("First Exam: "))
b = int(input("Second Exam: "))
c = int(input("Passing Grade: "))
d = (a*0.40) + (b*0.60)

if d > c:
    print("congratulations successful")
elif d < c:
    print("unfortunately unsuccessful")
else:
    print("successful")