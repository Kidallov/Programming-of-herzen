import requests

urls = {
    "Текущая температура": "https://wttr.in/?format=%t",
    "Скорость ветра": "https://wttr.in/?format=%w",
    "Состояние погоды": "https://wttr.in/?format=%c"
}

for name, url in urls.items():
    response = requests.get(url)
    result = response.text.strip()

    if name == "Скорость ветра":
        result = result[1:]

    print(f"{name}: {result}")
