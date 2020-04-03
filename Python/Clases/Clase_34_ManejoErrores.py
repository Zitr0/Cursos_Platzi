'''




'''

countries = {
    'colombia': 49,
    'mexico': 122,
    'argentina': 43,
    'chile': 18,
    'peru':31
}

while True:
    country = str(input('Ingresa el nombre del país: ')).lower()

    try:
        print('La población de {} es : {} millones'.format(country, countries[country]))
    except KeyError:
        print('no tenemos el dato de la población de {}'.format(country))

        