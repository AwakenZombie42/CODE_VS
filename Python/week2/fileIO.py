file = open("fileIO.txt", "r");
print(file.read());
file.close();

file = open("data.txt", "w");
file.write("My name is Zaid and I am 19 years old.\nMy CGPA is 9.25.\nI loving Coding.");
file.close();

file = open("data.txt", "a");
file.write("\nI am a student, like no shit nigga.");
file.close();

# this creates a new file named data.txt if there is no file named data.txt
file = open("data.txt", "r");
print(file.read());
file.close();

# this creates a new file named new.txt and writes the content give below
file = open("new.txt", "w");
file.write("My name is Zaid and I am 19 years old.\nMy CGPA is 9.25.\nI loving Coding.");
file.close();

with open("fileIO.txt", "r") as file:
    data = file.read();

with open("fileIO.txt", "w") as file:
    file.write(data + "\nI am a student, like no shit nigga.");

file = open("fileIO.txt", "r");
file.read(25);

# this creates a new file named new1.txt this will give and error if you run it while the file already exists
# file = open("new1.txt", "x");
