# перша програма/ Для кава-брейків на конференції закуплено круасани, стаканчики та пакунки кави. Ціна круасана — $1.04, ціна стаканчика — $0.34, ціна пакунка кави — $4.42. Потрібно скласти програму, яка обчислює, скільки повних доларів пішло на закупівлю їжі для кава-брейків і яка її повна вартість у центах.

price_croissant = 1.04
price_cup = 0.34
price_coffe = 4.42

quantity_croissant = int(input('введіть кількість круасанів: '))
quantity_cup = int(input('введіть кількість стаканчиків: '))
quantity_coffe = int(input('введіть кількість кави: '))

count_croisant = quantity_croissant * price_croissant
count_cup = quantity_cup * price_cup
count_coffe = quantity_coffe * price_coffe

all_sum_dollar = count_croisant + count_cup + count_coffe

all_sum_cent = all_sum_dollar * 100

print(f'сума круасанів: {round(count_croisant, 2)}$')
print(f'сума cтаканчиків: {round(count_cup, 2)}$')
print(f'сума кохфе: {round(count_coffe, 2)}$')
print(f'загальна сума: {all_sum_dollar}$ або {all_sum_cent}¢')


















































































