# Create a dictionary called students, that contains 3 students dictionaries 
# Student must be a dictionary as described in slide #12
# Iterate trough students and print average grade in the format: “The student_name has average grade of average_grade”
# student_name -> The name entered for the student
# average_grade -> The calculated average of all grades



students = {
    "student_first":{"name":"ivan","grades" : [100,90,80,70,10]},
    "student_second":{"name":"pesho","grades" : [80,60,40,30,20]},
    "student_third":{"name":"nikola", "grades" : [90,40,30,20,90]},
}

for key, attributes in students.items():
    total = 0
    # name is the current key
    # attributes is the current value which is a map.
    # So, we can index it to get the grades and iterate
    # over them.
    for grade in attributes["grades"]:
        total = total + grade
    average = total / len(attributes["grades"])
    print("The ", attributes["name"], " has average grade of ", average)