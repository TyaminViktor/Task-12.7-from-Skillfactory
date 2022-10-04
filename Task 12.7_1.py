per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("введите значение суммы вклада "))
per_cent = list(per_cent.values())
deposit = max([round(pc*money, 2) for pc in per_cent])
print("Максимальная сумма, которую вы можете заработать — ", deposit)
