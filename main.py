fruits = ["papaya", "watermelon", "mango"]
print(fruits[0])
fruits.append("apple")
print(fruits)
fruits.insert(1, "banana")
print(fruits)
fruits[2] = "kiwi"
print(fruits)
fruits.remove("papaya")
print(fruits)
print(len(fruits))
fruits.reverse()
print(fruits)
cut = fruits[0:2]
print(cut)

student = {"name": "Amit", "age": 12, "class": 9}
print(student["name"])
student["marks"] = 92
print(student)
student["age"] = 14
print(student)
del student["class"]
print(student)
print(student.keys())
print(student.values())


student_list = [
    [1, "Amit", "A"],
    [2, "Neha", "B"],
    [3, "Ravi", "A"],
    [4, "Pooja", "c"],
    [5, "Karan", "B"]

]

student_dict = {}

for student in student_list:
    roll_no = student[0]
    name = student[1]
    grade = student[2]
    student_dict[roll_no] = {"Name": name, "Grade": grade}

    print("Students Dictionary")
    print(student_dict)