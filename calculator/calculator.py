import random
while True:
    N = int(input("Напишите 1, если хотите чтобы калькулятор выбрал случайные значения. Напишите 2, если хотите написать значения сами: "))
    if N == 1:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        number = random.randint(0, 7)
        print(f"Количество упоковок: {num1}, стоимость: {num2}$")
    elif N == 2:
        num1 = int(input("Напишите количество упаковок: "))
        num2 = int(input("Напишите стоимость: "))
        number = int(input("Напишите действие: "))

        if num1 > 100 or num2 > 100:
            print("Проверьте количество материала!")
            continue
        else:
            True

    def calkulator(a, b, numb):
        print(f"Выбранное действие: {number}")
        if numb == 1:
            return f"Сложение: {a+b}"
        elif numb == 2:
            return f"Вычитание: {a-b}"
        elif numb == 3:
            return f"Умножение: {a*b}"
        elif numb == 4:
            return f"Деление: {a/b}"
        elif numb == 5:
            return f"Возведение в степень: {a**b}"
        elif numb == 6:
            return f"Остаток от деления: {a%b}"
        elif numb == 7:
            return f"Целочисленное деление: {a//b}"
        elif numb == 0:
            raise SystemExit("Выход")
            
        else:
            return "Нет такой комманды"

    print(calkulator(num1, num2, number))
