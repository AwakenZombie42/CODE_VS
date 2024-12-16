num = 12
deno = int(input("Enter the denominator: "));

try:
    result = round(num/ deno, 4);
    print(result);
except :
    print("Denominator should not be zero.");


# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "));
    assert num % 2 == 0;
except:
    print("Not a even number");
else:
    print(f"1/{num} or", round(1/num, 4));

'''
value = 123.456789
fixed_value = round(value, 4)
print(fixed_value)  # Output: 123.4568

value = 123.456789
fixed_value = f"{value:.4f}"
print(fixed_value)  # Output: 123.4568

fixed_value = float(f"{value:.4f}")
print(fixed_value)  # Output: 123.4568
'''