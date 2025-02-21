print("Enter Your Grades to Percentage")

math = int(input("Enter Average For Math: "))

science = int(input("Enter Average For Science: "))

english = int(input("Enter Average For English: "))

history = int(input("Enter Average for History: "))

#part

sum = math + science + english + history

print("Sum of Math, Science, English and History")

perc = (sum/400) * 100

print("Percentage Mark  ", perc)