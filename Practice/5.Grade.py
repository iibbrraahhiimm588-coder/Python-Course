marks = int(input("Enter Your Marks: 90"))

if (marks <= 50):
    print('Your grade is C')
elif(marks >= 50 and marks <= 75 ):
    print("YOUR GRADE IS B")
elif(marks >= 76 and marks <= 87):
    print("Your grade is A")
elif(marks >= 87):
    print("Your grade is A1")
else:
    print('You are failed')