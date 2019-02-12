from my_module import module



student_name = ""
students_dict = {}

while True:
    student_name = input("Write a student name: ")
    
    if student_name == "STOP":
        break
    
    grades = input("Input the integer grades separated by _: ")
    grades = grades.split("_")

    students_dict = module.add_entry(student_name,students_dict,grades)

    print (students_dict)
    print("---------------------------------------------------------")
