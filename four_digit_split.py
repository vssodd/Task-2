four_digit = input('Enter a four-digit number: ')

print(int(four_digit) // 1000)          # Thousands place
print(int(four_digit) // 100 % 10)      # Hundreds place
print(int(four_digit) // 10 % 10)       # Tens place
print(int(four_digit) % 10)             # Units place
