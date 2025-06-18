password = int(input("Enter the password: "))

password_length = len(str(password))

if password_length == 1:
    l = 10
elif password_length == 2:
    l = 100
elif password_length == 3:
    l = 1000
elif password_length == 4:
    l = 10000

for i in range(l):
    guess = i
    if password == guess:
        print("Access Granted")
        break