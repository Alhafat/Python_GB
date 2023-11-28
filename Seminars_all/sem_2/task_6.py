"""
Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е. +/-
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. +
✔ После каждой третей операции пополнения или снятия начисляются проценты - + 3% к депозиту
✔ Нельзя снять больше, чем на счёте  +
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой +
операцией, даже ошибочной
✔ Любое действие выводит сумму денег +
"""


def show_dep(dep):
    print(dep)


def nalog(dep):
    if dep >= 5_000_000:
        dep *= 0.9
    return dep


def amount_of_money(dep, temp):
    if temp > dep:
        print("Недостаточнор средств")
        show_dep(dep)
        main()


def withdrawal_tax(dep, temp, count):
    if 30 <= temp <= 600 and temp % 50:
        dep = dep - temp * 0.985
        if count == 3:
            dep += dep * 0.03
            count = 0
            show_dep(dep)
            return dep, count
        return dep
    else:
        print("Введена неверная сумма для снятия")
        show_dep(dep)
        main()


def main():
    count = 0
    dep: int = 10_000_000
    temp = int(input("Введите сумму на снятие: "))
    dep = nalog(dep)
    amount_of_money(dep, temp)
    dep, count = withdrawal_tax(dep, temp, count)


if __name__ == '__main__':
    main()
