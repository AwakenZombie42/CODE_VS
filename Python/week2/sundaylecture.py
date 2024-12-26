greet = lambda name: print(f"Hello, {name}!!!")
greet("John");

list1 = [1, 2, 3, 4, 5]

list2 = list(filter(lambda x: (x % 2 == 0), list1))
print(list2)

list3 = [1, 2, 3, 4, 5]

list4 = list(map(lambda x: x*2, list3))
print(list4)