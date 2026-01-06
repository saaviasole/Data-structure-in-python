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