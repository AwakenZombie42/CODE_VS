list1 = [1, 2, 3, 4, 5]

for i in list1:
    list1 = i * i
print(list1)

list2 = [1, 2, 3, 4, 5]
new_elements = []
for i in list2:
    if i % 2 == 0:
        new_elements.append(i * i)
list2.extend(new_elements)
print(list2)

list3 = [1, 2, 3, 4, 5]
list3.extend([i * i for i in list2 if i % 2 == 0])
print(list3)


def addition(a = 10, b = 20):
    return a + b
print(addition(10, 20))
print(addition(10))
print(addition())

def emp_info(first_name, last_name):
    return "First name " + first_name + " Last name " + last_name + "."
print(emp_info("Raj", "Kumar"))
print(emp_info(last_name = "Kumar", first_name = "Raj"))

def add(*args): # arbitrary arguments
    for i in args:
        print(i)
add(1, 2, 3, 4, 5, "hello")

def my_func(**kwargs): # arbitrary keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_func(first_name = "Raj", last_name = "Kumar", age = 25)

dict1 = {"key": i * i for i in [1, 2, 3, 4, 5]}
print(dict1)