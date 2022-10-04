per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("введите значение суммы вклада"))
deposit = round(max(per_cent.values())*money, 2)
print("Максимальная сумма, которую вы можете заработать — ", deposit)
