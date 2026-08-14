def welcome():
    print("Welcome to Python")

def greet(name):
    print("Hello.", name)

def square():
    return 5 * 5

def add(a, b):
    return a + b

welcome()
greet("Mozib")

result1 = square()
print("Square =", result1)

result2 = add(10, 20)
print("Sum =", result2)

a = int(input("Enter first number: "))
b = int(input("Enter second number.: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)

for i in range(1, 6):
    print(i)  

    
for i in range(1, 6,2):
    print(i)  
