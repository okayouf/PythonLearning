names = ['hawkeye', 'iron man', 'thor']
upper_names = [name.upper() for name in names]
print(upper_names)

num_letters = [(letter, number) for letter in 'ab' for number in range(3)]
print(num_letters)

words = {name : len(name) for name in names}
print(words)

def countdown(n):
    while n >= 1:
        yield n
        n -= 1
test = list(countdown(3))

print(test)