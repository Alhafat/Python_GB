"""
task_1
"""

# n = int(input())
# count = 0
# e = 2
# for i in range(1, n):
#     if i % e != 0 and i % 2:
#         count += i
# else:
#     print(count)

"""
task_2
"""

# number = int(input("1-999:\n"))
# number_1 = number
# count = 0
# while number > 0:
#     number //= 10
#     count += 1
# # print(count)
# match count:
#     case 1:
#         print(number_1 ** 2)
#     case 2:
#         temp = number_1 % 10 * (number_1 // 10)
#         print(temp)
#     case 3:
#         temp = (number_1 % 10) * 100 + number_1 // 10 % 10 * 10 + number_1 // 100
#         print(temp)
#     case _:
#         print("Неверное значение.")

#
# если делать со строкой
number = input("1-999:\n")
if 1 <= int(number) <= 999:
    match len(number):
        case 1:
            print(int(number).__pow__(2))  # степень
        case 2:
            print(eval("*".join(number)))  # перемножение
        case 3:
            print("".join(reversed(number)))  # разворот
else:
    print("Неверное значение.")
