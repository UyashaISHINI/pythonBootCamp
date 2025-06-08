marks=[95,67,78,89,78,93,65,24,34,56]
grades = []
for mark in marks:
    if mark>=90:
        grades.append("A")
    elif mark >= 80:
        grades.append("B")
    elif mark >= 70:
        grades.append("C")
    elif mark >= 60:
        grades.append("D")
    else:
        grades.append("F")

print("Student Marks and grades : ")
for i in range(len(marks)):
    print(f"student : {i+1} marks : {marks[i]} Grade : {grades[i]}")