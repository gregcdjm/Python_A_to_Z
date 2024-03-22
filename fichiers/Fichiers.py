#file = open("students.txt", "a+")
#file.write("Paul\n")
#file.write("Edouard\n")
#file.close()
students_list = ["Paul", "Louis", "Mathieur"]

with open("fichiers./students.txt", "w+") as file:
    for student in students_list:
        file.write(student + "\n")
    file.close()
