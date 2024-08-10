'''
Create a dictionary that stores the following information about a student:

    Name: "John Doe"
    Age: 21
    Major: "Computer Science"
    GPA: 3.8

Write a function update_gpa(student_dict, new_gpa) that updates the student's GPA.
Add a new key-value pair to the dictionary for the student's graduation year.
'''

student = dict()
student["Name"] = "John Doe"
student["Age"] = 21
student["Major"] = "Computer Science"
student["GPA"] = 3.8
print(f'student dictionary: {student}')

def update_gpa(student_dict, new_gpa):
    student_dict.update(new_gpa)
    return student_dict

print(f'updated student GPA: {update_gpa(student,{"GPA":3.7})}')

student.update({"Year":2019})
print(f'added graduation year: {student}')