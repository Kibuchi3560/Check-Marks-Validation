# print("Hello World")

# age = 16

# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")

a = [2, 2, 31, 5, 5]
def count_odd(list):
    l = list[:]
    c = 0
    while c < len(l):
        a = l[c]
        if a % 2 == 0:
            l.pop(c)
            print(l)
        else:
            c += 1
    return l

result = count_odd(a)
print("Odd numbers:", result)

def even_numbers(l):
    even = []
    for n in l:
        if n % 2 == 0:
            even.append(n)
            print(f"{n} is even")
    return even

result = even_numbers(a)
print("Even numbers:", result)