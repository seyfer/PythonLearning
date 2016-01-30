magicNumber = 42;

# one string comment

'''
multi line comment
'''

for x in range(101):
    if x == magicNumber:
        print(x)
        break
    else:
        print(x)

numbers = [1, 5, 11, 12, 13, 17]

print("numbers:")

for x in range(1, 20):
    if x in numbers:
        continue
    print(x)
