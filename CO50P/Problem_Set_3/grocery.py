grocery_list = {}

print("Please enter grocery items (press Ctrl-D to finish):")

while True:
    try:
        item = input().strip().upper()

        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        break

sorted_items = sorted(grocery_list.keys())
for item in sorted_items:
    print(f"{grocery_list[item]} {item}")
