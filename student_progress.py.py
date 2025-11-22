#  Student Information input
print("______________________________________")
print("______________________________________")
print("Student Progress Tracker (Mini App)")
print("______________________________________")
print("______________________________________\n")

print('"Enter the Student information"\n')
a = (input("Enter the name: "))
b = int(input("Enter the age: "))
c = (input("Enter the class: "))
e = int(input("Enter the Roll No: "))
d = int(input("Enter the subject number: "))

# subject marks

marks = []
for i in range(d):
    print("Enter the marks")
    m = float(input("Marks : "))
    marks.append(m)

# For validation
    if m < 0 or m > 100:
      print("Invalid marks! Please enter between 0–100")
      exit()



#  Calculations

total = 0
highest = 0
lowest = 100

total = sum(marks)

average = total / d

highest = max(marks)
lowest = min(marks)

# student marks count to grade

if average >= 90 and average <= 100:
    Grade = '"Excellent"'
elif average >= 75:
    Grade = '"Good"'
elif average >= 40:
    Grade = '"Average"'
else:
    average < 40
    Grade = '"Needs Improvement"'


# marks in reverse order 

question = (input("\nDo you want to see marks in reverse order? (yes/no): "))

# print to all codes  
print("\n________________________________") #the line only for design
print('"All Student Information"')  
print("-----------------------------------")         
print("Student Name is: ",a)
print("Student Age is: ",b)
print("Student Class is: ",c)
print("Total subject is: ",d,)
print("__________________________\n")
print('"Student marks"')
print ("Total marks: ",total)
print("highest marks: ",highest)
print("lowest marks: ",lowest)
print ("Average marks",average)
print("Grade: ",Grade,"\n")
print("___________________________________________________\n")

# match case code

match question:
    case "yes":
        print("Reverse Order marks",marks[::-1])
        print("\n_____________________________________________________________________")

    case "no":
        print('"Thank you "')
        print("____________________")

    case _:
        print("Invalid Input")

