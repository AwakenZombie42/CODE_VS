# Dictionary

print("Dictionary\n");

dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
};

print(dictionary,"\n");
print(dictionary.keys(),"\n");
print(dictionary.values(),"\n");
print(dictionary["name"],"\n");
print(dictionary["age"],"\n");
print(dictionary["city"],"\n");

dictionary["age"] = 31;

print(dictionary["age"],"\n");

# Nested Dictionary

family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
};

print(family["child1"]["name"],"\n");
print(family["child2"]["name"],"\n");
print(family["child3"]["name"],"\n");

# Dictionary Comprehension

numbers = [1, 2, 3, 4, 5];
squares = {num: num * num for num in numbers};
print(squares,"\n");

# Dictionary Methods

print(len(dictionary),"\n");
print("name" in dictionary,"\n");
print("name" not in dictionary,"\n");

dictionary.clear();
print(dictionary,"\n");

# Sets

print("Sets\n");

Student = {"Zaid", "Shaikh", "Z", "Zaid"};
print(Student,"\n");
print(len(Student),"\n");
print("Z" in Student,"\n");
print("Z" not in Student,"\n");

# Set Comprehension

numbers = [1, 2, 3, 4, 5];
even_numbers = {num for num in numbers if num % 2 == 0};
print(even_numbers,"\n");

companies = {'Lacoste', 'Ralph Lauren'};
tech_companies = ['apple', 'google', 'apple'];
companies.update(tech_companies);
print(companies,"\n");

#Set Operations

A = {1, 2, 3, 4, 5};
B = {4, 5, 6, 7, 8};

print(A.union(B),"\n");
print(A.intersection(B),"\n");
print(A.difference(B),"\n");
print(A.symmetric_difference(B),"\n");

# tuple

print("Tuple\n");

# Frozenset

print("Frozenset\n");

fs = frozenset([1, 2, 3, 4]);
print(fs,"\n");
print(len(fs),"\n");
print(2 in fs,"\n");
print(5 in fs,"\n");

my_tuple = (1, 2, 3, 4, 5);
print(my_tuple,"\n");
print(len(my_tuple),"\n");
print(2 in my_tuple,"\n");

# tuple Comprehension

numbers = [1, 2, 3, 4, 5];
even_numbers = tuple(num for num in numbers if num % 2 == 0);
print(even_numbers,"\n");

# tuple Methods

print(len(my_tuple),"\n");
print("2" in my_tuple,"\n");
print("2" not in my_tuple,"\n");
print(my_tuple.count(2),"\n");
print(my_tuple.index(2),"\n");

# tuple unpacking

a, b, c, d, e = my_tuple;
print(a,"\n");
print(b,"\n");
print(c,"\n");
print(d,"\n");

# tuple Slicing

print(my_tuple[1:4],"\n");
print(my_tuple[:3],"\n");
print(my_tuple[3:],"\n");