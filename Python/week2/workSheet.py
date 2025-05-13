'''
1. Working with Dictionaries
Write a Python program that does the following:
• Create e dictionary to store information about a book (title, author, price).
• Add a new key-value pair for the year of publication.
• Update the price of the book
• Print all the keys and values in the dictionary using a loop.
'''
print("Question 1")
book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "price": 10.99,
}
book["year"] = 1925
book["price"] = 12.99

print("Book Information:")
for key, value in book.items():
    print(f"{key}: {value}")

'''
2. Sets and Lists
Write a Python program to.
Create a list of integers wth some duplicate values_
Convert the list into a set to remove duplicates.
Add three more unique values to the set.
Convert the set back into a sorted list and print the result
'''
print("\nQuestion 2")
numbers = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10]
unique = set(numbers)
unique.add(11)
unique.add(12)
unique.add(13)
unique = sorted(list(unique))
print(unique)

'''
3. Loops with Conditional Statements
Write a Python program to find the prime numbers between 10 and 50 using a loop.
Use a for loop to check each number in the range.
Use a nested loop or conditions to check if the number is prime.
Print the prime numbers.
'''
print("\nQuestion 3")
for num in range(10, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

'''
4. Exception Handling
Write a Python program that
Takes two numbers as input from the user.
Divides the first number by the second.
Handles the ZeroDivisionError with a custom error message.
Handles the ValueError if the user enters non-numeric input.
'''
print("\nQuestion 4")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero.")

'''
5. File Handling
Write a Python program to.
Create a text file called students . txt_
Write the names of 5 students into the file (one name per line).
Read the file and print each name with its line number (e.g., "1: John").
Ensure the file is properly closed after both writing and reading operations.
'''
'''
print("\nQuestion 5")
with open("students.txt", "w") as file:
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    for name in enumerate(names, start=1):
        file.write(f"{name}\n")

with open("students.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}: {line.strip()}")
'''
print("\nQuestion 5")
file = open("students.txt", "w")
file.write("Alice\nBob\nCharlie\nDavid\nEve")
file.close()

file = open("students.txt", "r")
for i, line in enumerate(file, start=1):
    print(f"{i}: {line.strip()}")
file.close()