subjects = ["Math", "Science", "English", "History", "Geography"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter the marks for {subject}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(subjects)
if average >= 90:
    grade = 'A1'
elif average >= 80:
    grade = 'A2'
elif average >= 70:
    grade = 'B1'
elif average >= 60:
    grade = 'B2'
elif average >= 50:
    grade = 'C1'
elif average >= 40:
    grade = 'C2'
elif average >= 33:
    grade = 'D'
else:
    grade = 'F'

print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Grade: {grade}")