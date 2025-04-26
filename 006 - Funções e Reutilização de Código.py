def greet_user(name):
    print(f"Hello, {name}")
    
greet_user("Geovanna")
print()

def greet_user(name="Guest"):
    print(f"Hello, {name}")
    
greet_user()
greet_user("Geovanna")
print()

def calculate_area(length, breadth):
    return length * breadth

area = calculate_area(5,3)
print(f"The area of the rectangle is {area}")
print()

global_var = 10
print(f"Global variable before function call: {global_var}")

def modify_variable():
    global_var = 20
    print(f"Update global variable inside function: {global_var}")
    
modify_variable()
print(f"Global variable after function call: {global_var}")

def modify_global_variable():
    global global_var
    global_var = 20
    print(f"Update global variable inside function: {global_var}")
    
modify_global_variable()
print(f"Global variable after function call: {global_var}")
