def add(p,q):
    return p + q
def subtract (p,q):
    return p - q
def multiply(p,q):
    return p * q
def division(p,q):
    return p / q
print("please select the operation ")
print("A. add")
print("B. subtract")
print("C. multiply")
print("D. division")
choice= input("please enter choice (a/b/c/d)").lower()
num1 = int(input("Please enter the first number "))
num2 = int(input("please enter the second number "))
if choice == 'a':
    print(num1 , " + ", num2 , ' = ', add(num1,num2))
elif choice == 'b':
    print(num1 , " - ", num2 , ' = ', subtract(num1,num2))
elif choice == 'c':
    print(num1 , " * ", num2 , ' = ', multiply(num1,num2))
elif choice == 'd':
    print(num1 , " / ", num2 , ' = ', division(num1,num2))
else:
    print("please enter a correct choice")         