a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

print(a, b)  # Print original values

a = a + b
b = a - b
a = a - b

print(a, b)  # Print swapped values
