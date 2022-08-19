a = int(input("Enter your Accumulated Scores: "))
b = int(input("Enter your Midterm Scores: "))
c = int(input("Enter your Final Scores: "))
x=a+b+c

if (x>=80):
    print("A")
elif (x>=75):
    print("B+")
elif (x>=70):
    print("B")
elif (x>=65):
    print("C+")
elif (x>=60):
    print("C")
elif (x>=55):
    print("D+")
elif (x>=50):
    print("D")
else :
    print("F")