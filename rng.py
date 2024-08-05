import random

x = random.randrange(1, 9999999)

number_array = [int(digit) for digit in str(x)]
print("The list from number is:", number_array)

for i in range(len(number_array)):
    if number_array[i] % 2 == 0:
        y = random.randrange(30, 60)
        number_array[i] = chr(y)

password = ''.join(str(element) for element in number_array)
print("Generated password:", password)