def add_entry (student_name, student_dict, grades_list):
    int_grades = list()
    for arg in grades_list:
        value = int(arg)
        int_grades.append(value)
    student_dict.update({student_name : int_grades})      
    return student_dict


# student_name = ""
# students_dict = {}

# while True:
#     student_name = input("Write a student name ")
    
#     if student_name == "STOP":
#         break
    
#     grades = input("Input the integer grades separated by _: ")
#     grades = grades.split("_")

#     students_dict = add_entry (student_name, students_dict, grades)

#     print (students_dict)
#     print("---------------------------------------------------------")

