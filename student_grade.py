student_marks={
    "jenny":92,
    "harry":78,
    "dimpy":56,
    "rahul":41,
    "ankur":99,
    "prem":34
}
for student in student_marks:
    
    if student_marks[student]>90:
        student_marks[student]="A+"
    elif student_marks[student]>80:
        student_marks[student]="A"
    elif student_marks[student]>70:
        student_marks[student]="B+"
    elif student_marks[student]>60:
        student_marks[student]="B"
    elif student_marks[student]>50:
        student_marks[student]="c"
    elif student_marks[student]>40:
        student_marks[student]="D"
    else:
        student_marks[student]="F"
print(student_marks)
