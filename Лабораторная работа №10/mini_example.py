# импорт модулей
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# создаем класс, в котором отправляется запрос к ЦБ
class CBRRates:
    def __init__(self): # конструктор класса, который вызывается автоматически
        self.url = 'https://www.cbr.ru/scripts/XML_daily.asp' # url ЦБ
        self.rates = {} # создаем словарь, где будут хранится валюты
        self._fetch_rates() # функция, которая занимается отправкой запроса к ЦБ

    def _fetch_rates(self):
        try:
            response = requests.get(self.url) # get запрос к ЦБ
            response.raise_for_status() # проверка на успешный запрос
            tree = ET.fromstring(response.content) # используем fromstring, так как парсим не из файла на диске, а также деревом, откуда дальше мы берем элементы

            for valute in tree.findall('Valute'):
                char_code = valute.find('CharCode').text # берем код для каждого курса
                if char_code in ['USD', 'EUR', 'GBP']:
                    value = valute.find('Value').text # берем значение каждого кода

                    # Преобразуем значение к float, заменяя запятую на точку
                    rate = float(value.replace(',', '.'))
                    self.rates[char_code] = round(rate, 4) # берем значение по коду валюты и округляем значение до 4 знаков после запятой

        # Обработка ошибок
        except requests.RequestException as e:
            print(f"Ошибка при запросе к ЦБ РФ: {e}")
        except Exception as e:
            print(f"Ошибка обработки данных: {e}")

    def get_rate(self, currency):
        return self.rates.get(currency) # ищет в списке значение по ключу

    def __str__(self):
        return f"Курсы ЦБ РФ на {datetime.now().strftime('%d.%m.%Y')}: {self.rates}"


# Пример использования:
if __name__ == "__main__":
    rates = CBRRates()
    print(rates)  # Выведет словарь с курсами USD, EUR, GBP
    print("Курс доллара:", rates.get_rate('USD'))
