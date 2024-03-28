marks = float(input('Enter your marks: '))
if marks >=80 and marks <= 100:
    print("A+")
elif marks >= 70 and marks < 80:
    print("A")
elif marks >= 60 and marks < 70:
    print("A-")
elif marks >= 50 and marks < 60:
    print("B")
elif marks >= 40 and marks < 50:
    print("C")
elif marks >= 33 and marks < 40:
    print("D")
elif marks >= 0 and marks < 33:
    print("Fail")
else:
    print('Invalid marks')