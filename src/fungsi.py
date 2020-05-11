# FUNGSI

# print('Fikky')

# def salam(nama):
#     print('Assalamualaikum', nama)

# salam('Naruto')

# def pertambahan(bil1, bil2):
#     return bil1 * bil2

# print(pertambahan(34, 60))
# print(pertambahan(4, 3))
# print(pertambahan(9, 7))


def fib(n):
    a = 0
    b = 1
    for i in range(2):
        a, b = b, a + b
    
    return a

print(fib(2))

# for i in range(10):
#     print(i)

# a = b
# b = a + b

# a = 1
# b = 2