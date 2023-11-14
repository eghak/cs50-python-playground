##### if - elif #####

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

##### if - elif - else #####
# instead of using 'elif' for the last one, we can use 'else' to reduce runtime, less code, less checking.

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# 'or' & 'and' operators

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")


