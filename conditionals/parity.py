x = int(input("What's x? "))

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(x))

# simpler way
def is_even(num):
    return True if num % 2 == 0 else False

print(is_even(x))

# more simpler way
def is_even(num):
    return num % 2 == 0

print(is_even(x))