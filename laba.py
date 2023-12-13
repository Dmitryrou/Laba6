import requests

def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'lang': 'ru'  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    try:
        requeset = requests.get(make_url(city), make_parameters())
        return requeset.text
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if requeset.status_code == 200:
        return requeset.text
    else:
        return '<ошибка на сервере погоды>'                                

def acquaintance(names: str):
    if names != '': 
        print(f'Привет, {names}') 
    else:
        print('Вы не написали имя, я обиделась')
        exit()

def how_sity(sities: str):
    if sities != '':
        print(f'Погода в {sities}: {what_weather(sities)}')
    else:
        print('Вы не написали город, я обиделась')
        exit()


    

print(f'Меня зовут Анфиса и твой ассистент, я еще много не умею но быстро учусь')
name =  input('Как вас зовут?\n')          
acquaintance(name)
sity = input('Из какого вы города? \nЭто поможет мне выдавать информацию правильно.\n')
how_sity(sity)
print('2')
print('2')
print('2')

