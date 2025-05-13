# Sequence Data Type & Loops

languages = ["C", "C++", "Java", "Python"];

print(languages);
print(languages[0]);
# negative indexing means count from the last element
print(languages[-1]);
print(languages[0:2]);
print("Length of the list is: ", len(languages));

name = "Python";
print(name[0]);

'''
 String is immutable that means it can not be changed so this will give and error
 name[0] = "p";
 print(name[0]);
 TypeError: 'str' object does not support item assignment
'''
# For loop

List = [69, 70, 71, 72, 73, 74, 75];

for i in List:
    print(i, "\n");

for i in "Python":
    print(i, "\n");

for i in List:
    print(i * 10);
print();

for i in range(10): # end
    print(i);
print();

for i in range(10, 20): # start, end
    print(i);
print();

for i in range(10, 20, 2): # start, end, step
    print(i);

print();
#Sum of numbers from 1 to 10 use for loop in range
sum = 0;
for i in range(1, 11):
    sum = sum + i;
print("sum = ", sum);
print();

# break and continue
print("break");
for i in range(5):
    if i == 3:
        break;
    print(i);

print("continue");
for i in range(5):
    if i == 3:
        continue;
    print(i);
print();

# Nested loop
print("Nested loop");

for i in range(1, 6):
    for j in range(2, 6):
        print(f"{i} * {j} = {i * j}", end = "\t");
    print("\n");

n = 5;

'''
for i in range(n):
    for j in range(i):
        print("*", end = " "); #print(f"{j}", end = "");
    print("\n");
Even tho this look every smart to do, this is a really bad practice
https://chatgpt.com/share/675ed10c-e71c-8009-80b8-c2ea469afb6e
refer this to understand
'''

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end = " ");
    print("\n");