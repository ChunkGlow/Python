a = 30,000,000

print("type of a:", type(a))

b = 2500.7500

print("type of b:", type(b))

c = "DeskHub"

print("type of c:", type(c))

d = False

print("type of d:", type(d))

# 2nd

name = "Donald"

age = "8"

is_student = True

weight = 34.3

print("Name : ", name)

print("Data Type of Name is", type(name))

print("Age : ", age)

print("Data Type of Age is", type(age))

print("is_student : ", is_student)

print("Data Type of weight is", type(weight))

print("\n After Type Casting...")

age = str(age)

print(age)

print("Data Type of age is", type(age))

weight = int(weight)

print(weight)

# 3rd

text = str(input("Enter a String : "))

revText = text[::-1]

text = revText

print(text)