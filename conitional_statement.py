marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B.")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

for i in range(1, 6):
    print(i)  

age = 20

if age >= 18:
    print("You are anadult")
else:
    print("You are a minor")    

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)

print(fruits[0])

fruits.append("Grapes")

fruits.remove("Banana")

print(fruits)