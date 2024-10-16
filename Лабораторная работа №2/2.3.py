from functools import partial

# Словарь с радиоактивными изотопами и их периодами полураспада
isotopes = {
    'Uranium-238': 4.468e9,  # период полураспада в годах
    'Carbon-14': 5730,      # период полураспада в годах
    'Radon-222': 3.8,       # период полураспада в днях
}

# Функция для каррирования
def remaining_amount(N0, t1_2, t):
    return N0 * (1 / 2) ** (t / t1_2)

N0 = 1000  # Начальное количество вещества
t = 10000  # Время, за которое мы хотим узнать остаток (в годах)

for isotope, t1_2 in isotopes.items():

    calculate_remaining = partial(remaining_amount, N0, t1_2)
    remaining_N = calculate_remaining(t)
    print(f'От радиоактивного изотопа {isotope} после {t} лет осталось {remaining_N:.2f} единиц вещества.')
