# WHILE LOOPS

# n = 10

# while n > 0:
#     print(n)
#     n = n-1

print('Jika Ingin berhenti input -1')
user_input = int(input('Masukan nilai: >'))

nilai = []

while user_input > 0:
    nilai.append(user_input)
    user_input = int(input('Masukan nilai lagi: >'))

print('List Nilai', nilai)