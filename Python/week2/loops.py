# While loop
i = 1;
while i < 6:
    print(i);
    i += 1;

i = 5;
while i > 0:
    print(i);
    i -= 1;

counter = 0;

while counter < 2:
    print("Inside the loop");
    counter += 1;
else:
    print("Inside the else block");

i = 0;
while i < 5:
    if i == 3:
        break;
    print(i);
    i += 1;

i = 0;
while i < 5:
    if i == 3:
        i += 1;
        continue;
    print(i);
    i += 1;