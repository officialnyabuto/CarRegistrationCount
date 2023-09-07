import itertools

# Define the alphabet and numbers
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

# Initialize a counter for valid combinations
count = 0

# Generate and count valid combinations
for a, b, n1, n2, n3, l in itertools.product(alphabet, alphabet, numbers, numbers, numbers, alphabet):
    if '000' not in n1 + n2 + n3:
        count += 1

print("Number of valid combinations:", count)