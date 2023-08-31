PATH = r"C:\Users\Admin\Desktop\Karan\PYTHON\School Project\Practical File\Files\datafile.txt"

def process_file():
    data = []
    with open(PATH, "r") as f:
        for line in f:
            userdata = line.strip("\n").split()
            data.append(tuple(userdata))
    return data

def sort_students_number():
    data = process_file()
    return sorted(data, key=lambda x: int(x[2]))

def filter_students_year():
    data = process_file()
    return [student[0] for student in data if int(student[3]) < 3]

def no_people_department():
    data = process_file()
    return {
        dept: sum([1 for student in data if student[4] == dept])
        for dept in set([student[4] for student in data])
        }

print(*process_file(), sep="\n")
print(sort_students_number())
print(filter_students_year())
print(no_people_department())