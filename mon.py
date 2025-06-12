li=['apple','mango','avacado']
obji=enumerate(li)
print(list(obji))

class Employee:
    def __init__(self):
        print("Employee was created")
    
    def __init__(self):
        print("The created employee was destroyed")
def create_obj():
    print("Making object....")
    obj=Employee()
    print("Function end....")
    return obj
print("Calling create_obj() function ....")
obj=create_obj()
print("Programe ends.....")
