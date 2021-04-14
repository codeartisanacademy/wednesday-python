indonesia = {
    # KEY - VALUE PAIR
    'official_name': 'Republic of Indonesia',
    'president': 'Joko Widodo',
    'capital': 'Jakarta',
    'population': 250000000,
    'states': ['Jawa Barat', 'DKI Jakarta', 'Jawa Tengah', 'Sumatera Utara'],
    'ministers' : [
        {'Ministry of State Secretariat':'Pratikno'},
        {'Ministry of Home Affairs':'Tito Karnavian'},
        {'Ministry of Foreign Affairs':'Retno Marsudi'}
    ]
}

print(indonesia["president"])

indonesia['population'] = 250000000

for k in indonesia.keys():
    print(k)

for v in indonesia.values():
    print(v)

indonesia['population'] = 240000000

print(indonesia["population"])

for state in indonesia['states']:
    print(state)

for minister in indonesia['ministers']:
    for k in minister.keys():
        print("{0} - {1}".format(k, minister[k]))

